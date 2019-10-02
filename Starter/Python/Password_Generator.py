import random

StrH="QWERTYUIOPASDFGHJKLZXCVBNM"
StrL="qwertyuiopasdfghjklzxcvbnm"
Num="1234567890"
Special="@#&"


def encrypt(str,key):
    rt=""
    y=0

    for i in range(len(str)):
        if(y>len(key)-1):
            y=0
        rt=rt+chr(ord(str[i])+ord(key[y]))
        y=y+1

    return rt
def decrypt(str,key):
    rt=""
    y=0
    for i in range(len(str)):
        if(y>len(key)-1):
            y=0
        rt=rt+chr(ord(str[i])-ord(key[y]))
        y=y+1
    return rt



def Passw(Length):
    nu=random.randint(4,Length-4)
    password=""
    password=password + ''.join(random.choice(StrH) for i in range(nu-2))
    password=password + ''.join(random.choice(StrL) for i in range(Length-nu-2))
    password=password + ''.join(random.choice(Special))
    password=password + ''.join(random.choice(Num) for i in range(3))
    return password

try:
    pas=open("data.en","r")
except:
    pas=open("data.en","a",encoding="ISO-8859-1")
    print("This program is runnning first time in this directory please set a main password")
    mai=input("\t")
    pas.write(encrypt(mai,mai)+"\n")
    pas.close()
    print("Please restart the program ")
    input()
    exit()

pas.close()

pa=open("data.en","r" , encoding="ISO-8859-1")
y=pa.read().split("\n")[0]
print("\tPlease enter password\n ")
test=input("\t")
if not (y==encrypt(test,test)):
    print("\n\tPassword Wrong")
    input()
    exit()
pa.close()

while True:
    print("\n\tEnter choice \n\ta: Create new password \n\tb: Search for password \n\tc: Exit program \n")
    y=input("\t")
    if (y=="a"):
        pa=open("data.en","a",  encoding="ISO-8859-1")
        print("\tEnter name of website \n")
        web=input("\t")
        print("\tEnter length of password min 8")

        while True:
            try:
                n=int(input("\t"))
                break
            except:
                print("\tPlease enter integer")
                continue

        if n < 8:
            print("\tPassword cant be less than 8 ")
            exit("\t\tERROR")
        while True:
            y=''.join(random.sample(Passw(n),n))
            print("\tPassword generated is " +y )
            print("\tok ? y/n")
            if input("\t").lower()=="y":
                break
            else:
                continue

        pa.write(encrypt(web.upper(),test)+" "+ encrypt(y,test)+"\n")
        pa.close()

    elif(y=="b"):
        print("\tTo break the Loop enter exit\n\n")
        while True:
            pa=open("data.en","r",encoding="ISO-8859-1")
            print("\tWebsite name to search for \n")
            f=input("\t").upper()
            if f=="EXIT":
                break
            f=encrypt(f,test)
            if (f in open("data.en","r",encoding="ISO-8859-1").read()):
                for line in pa :
                    if (line.split()[0]==f):
                        print("\n\tpassword of website is " + decrypt(line.split()[1],test)+"\n")
            else:
                print("\n\twebsite not in database \n")


    else:
        exit("\n\n\n\t\tThank you")
