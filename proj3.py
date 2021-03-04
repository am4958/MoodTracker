import socket
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
UDP_IP = "192.168.1.172" 
SHARED_UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
sock.connect((UDP_IP, SHARED_UDP_PORT))
numofmoods = 0
moodhist = []
colors = []

##initial message
print("Please enter your mood on a scale from 1-9") 
def loop():
>-------while True:
>------->-------data = sock.recv(2048)
#>------>-------print(data)
>------->-------moodnum = [int(s) for s in data.split() if s.isdigit()]
>------->-------if moodnum:
>------->------->-------organizedFunc(moodnum)


##repreats for each round of score
def myFirstFunc():
>-------print("Please enter your mood on a scale from 1 - 9")
>-------print(" ")

###organizational for func orders
def organizedFunc(moodnum):
>-------global numofmoods
>-------moodhist.append( moodnum[0])
>-------print("Your current mood is stored as: " + str(moodhist[numofmoods]))
>-------print(" ")
>-------numofmoods +=1
#>------print(numofmoods)
>-------toosad(moodhist)
>-------moodchart(moodhist)
>-------myFirstFunc()


##if mood is below a 5 the user gets a check in message

def toosad(moodhist):
>-------lastnum = numofmoods-1
>-------if moodhist[lastnum] < 5:
>------->-------print("You okay bud?")
>------->-------print(" ")


##creates plot of mood for past 10 hrs
def moodchart(moodhist):
>-------global numofmoods
>-------if numofmoods == 10:
>------->-------barcolors(moodhist)
>------->-------avgmood(moodhist)
#>------>-------print(moodhist)
>------->-------hours = ('0', '1', '2', '3', '4','5','6', '7', '8', '9')
>------->-------y_pos = np.arange(len(hours))
>------->-------plt.bar(y_pos, moodhist, align='center', alpha=0.5, color = colors)
>------->-------plt.xticks(y_pos, hours)
>------->-------plt.ylabel('Mood Score')
>------->-------plt.xlabel('Hour')
>------->-------plt.title('Your Mood Chart')
>------->-------plt.show(block=False)
>------->-------plt.pause(10)
>------->-------numofmoods = 0
>------->-------moodhist.clear()
>------->-------plt.close()

##prints avg mood for the day

def avgmood(moodhist):
>-------total = 0
>-------for mood in moodhist:
>------->-------total += mood
>-------avgmood = total/len(moodhist)
>-------print ("Your average mood is: "+ str( avgmood))#CHANGE IF CHANGE NUM OF MOODS IN CHART
>-------if avgmood < 5:
>------->-------print("checking in on you dude, maybe you should phone a friend")


##sets barchart colors based on mood score
def barcolors(moodhist):
>-------global colors
>-------for mood in moodhist:
>------->-------if mood > 6:
>------->------->-------colors.append("green")
>------->-------if mood > 3:
>------->------->-------colors.append("orange")
>------->-------else:
>------->------->-------colors.append("red")

if __name__ == "__main__":
>-------sock.send('Hello ESP32'.encode())
>-------loop()

