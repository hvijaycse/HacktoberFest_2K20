# importing required library
import threading
import socket
import time

#declaring globl variables
global Running
global s
port=9999

#lets create a socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # ipv4 and udp protocoal
Running=True # this will be used to stop threads

# defing functions for reciving ans sending meassages

def Reciver(name):
    while Running:
        try:
            message=s.recvfrom(125)[0].decode('ascii')
        except:
            break
        if '$$$' in message:
            print("\n"+name[0:-2]+" exited press Enter to exit")
            s.close()
            break
        print('\n'+ name+": "+message)
    return

def Sender(soc):
    message=input("Enter Message: ")
    try:
        s.sendto(message.encode('ascii'),soc)
    except:
        return
    if '$$$' in message:
        ret=False
        s.close()
        time.sleep(0.5)
    else:
        ret=True
    return ret


# now time for main function
Running=True
print("Input $$$ to exit the chat\n")
select=input("Reciver(r) or Sender(s) :").lower()

if select=='s':
    IP=input("Please Enter Reciver ip :")
    soc=(IP,port)
    s.sendto('Connected'.encode('ascii'),soc)
    print(s.recvfrom(125)[0].decode('ascii'))
    rec=threading.Thread(target=Reciver,args=("Reciver :",))
    rec.start()
    while rec.isAlive() :
        Running=Sender(soc)
    rec._stop()
    rec.join()
    print("\n\n\tBYEBYE")
    exit(0)
elif select=='r':
    IP=socket.gethostbyname(socket.gethostname())
    print("My IP: ",IP)
    try:
        s.bind((IP,port))
    except:
        print("\tYour port",port,"is busy please close another service running on this\n\tport or change port number in this program.")
        input()
        exit(1)
    print("Waiting for Sender")
    message,soc=s.recvfrom(125)
    s.sendto("Connected".encode('ascii'),soc)
    print(message.decode('ascii'))
    rec=threading.Thread(target=Reciver,args=("Sender :",))
    rec.start()
    while rec.isAlive() :
        Running=Sender(soc)
    rec._stop()
    rec.join()
    print("\n\n\tBYEBYE")
    exit(0)

else:
    print("Wrong option exiting program")
    exit(0)

#Truly even i dont understand this program completly
