
from email.policy import default
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def PortScanner(HOST,port):
    #checking if port is opened or closed
    if s.connect_ex((HOST, int(port))):
        print(f"The port is closed {port}")
    else:
        print(f"The port is open {port}")

def main():
    print("WELCOME TO MY CONSOLE CYBERSECURITY APPLICATION")
    print("<--------------------------->")
    print('What do you wanna make today?')
    print('1 - SCAN PORTS')
    print('0 - Close Application')
    choice = int(input())
    match choice: 
        case 1:
            print('Do you wanna scan')
            print('1 - A single port')
            print('2 - A range of ports')
            choice = int(input())
            match choice:
                case 1:
                    HOST = input("ENTER THE IP ADDRESS: ")
                    PORT = str(input("ENTER THE PORT: "))
                    PortScanner(HOST, PORT)
        case 0:
            pass
    print('--------------------------------')
    print('Thank you for use my application')
main()