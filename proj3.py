# a python program to send an initial packet, then listen for packets from the ESP32
import socket
UDP_IP = "192.168.1.172" # The IP that is printed in the serial monitor from the ESP32
SHARED_UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
sock.connect((UDP_IP, SHARED_UDP_PORT))
numofmoods = 0
curmood = []
print("Please enter your mood on a scale from 1-10") #fix for 10
def loop():
>-------while True:
>------->-------data = sock.recv(2048)
>------->-------print(data)

>------->-------moodnum = [int(s) for s in data.split() if s.isdigit()]
>------->-------if moodnum:
>------->------->-------organizedFunc(moodnum)

def myFirstFunc():
>-------print("Please enter your mood on a scale from 1 - 10")


def organizedFunc(moodnum):
>-------global numofmoods
>-------curmood.append( moodnum)
>-------print(curmood)
>-------print("Your current mood is stored as: " + str(curmood[numofmoods]))
>-------numofmoods +=1
>-------print(numofmoods)
>-------if numofmoods >4:
>------->-------print("Here is your mood chart")
>------->-------for num in curmood:
>------->------->-------print(num)
>-------myFirstFunc()




if __name__ == "__main__":
>-------sock.send('Hello ESP32'.encode())
>-------loop()
