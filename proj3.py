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
>-------moodhist.append( moodnum[0])
>-------print("Your current mood is stored as: " + str(moodhist[numofmoods]))
>-------numofmoods +=1
>-------print(numofmoods)
>-------toosad(moodhist)
>-------moodchart(moodhist)
>-------myFirstFunc()

def toosad(moodhist):
>-------lastnum = numofmoods-1
>-------if moodhist[lastnum] < 5:
>------->-------print("You okay bud?")

def moodchart(moodhist):
>-------global numofmoods
>-------if numofmoods > 2:
>------->-------print(moodhist)
>------->-------hours = ('0', '1', '2')
>------->-------y_pos = np.arange(len(hours))
>------->-------plt.bar(y_pos, moodhist, align='center', alpha=0.5)
>------->-------plt.xticks(y_pos, hours)
>------->-------plt.ylabel('mood')
>------->-------plt.xlabel('hours')
>------->-------plt.title('Your Mood Chart')
>------->-------plt.show(block=False)
>------->-------plt.pause(3)
>------->-------numofmoods = 0
>------->-------moodhist.clear()
>------->-------plt.close()





if __name__ == "__main__":
>-------sock.send('Hello ESP32'.encode())
>-------loop()

