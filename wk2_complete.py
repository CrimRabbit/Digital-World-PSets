# Import eBot and time module
from eBot import eBot
from time import sleep

def forward(speed, duration):
    # Write your code here
    ebot.wheels(speed,speed)
    sleep(duration)
    pass

ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth

############### Start writing your code here ################ 
#leftV, rightV, duration = input("Enter left wheel speed, right wheel speed, duration delimited by commas.")
speed, duration = input("Enter speed, duration delimited by commas.")
forward(speed, duration)
temp = ebot.temperature()
print "The returned temperature is "+str(temp)
########################## end ############################## 

ebot.disconnect() # disconnect the Bluetooth communication
