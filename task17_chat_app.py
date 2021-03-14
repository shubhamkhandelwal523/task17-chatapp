import socket
import os
import threading
import pyttsx3 as ps
from pyfiglet import Figlet

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

IP_address = input("Enter Your IP:")
port = 7877
receiver_ip=input('Receiver IP is:-')
receiver_port=int(input('Receiver Port No.:- '))
t=Figlet('puffy')
ps.speak("HEY! WELCOME TO MY CHAT APP")
print(t.renderText("\t\t CHAT APP !"))


s.bind((IP_address , port))

def receiver():
    while True:
        x = s.recvfrom(1024)
        if x[0].decode()=='exit' or x[0].decode()=='bye':
            print('\t\t\t\t\t Bye-Bye\n\n\n')
            s.sendto('exit'.encode(), (receiver_ip, receiver_port))
            os._exit(1)
        clientip = x[1][0]
        data = x[0].decode()
        print("\n\t " + clientip + ":" + data)


def sender():
    while True:
        s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        print()
        x = input("You: ")
        s.sendto(x.encode(),(receiver_ip,receiver_port))
        if(x=="bye" or x=="exit"):
                os._exit(1)


x1 = threading.Thread( target = receiver )
x2 = threading.Thread( target = sender)

x1.start()
x2.start()
