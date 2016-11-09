import RPi.GPIO as GPIO
import firebase
import time

fburl = "https://kivyled.firebaseio.com/"
token = "STPBn7iDLmuAITbCgSvAjVKV7HfzxBX1FyTSnzQj"

firebase = firebase.FirebaseApplication(fburl, token)

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO12, 16, 20 and 21 for the buttons.
buttons = {'red': 24, 'yellow': 23}

# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.
GPIO.setup(buttons.values(), GPIO.IN, GPIO.PUD_DOWN)

redStatus = firebase.get('/redLed')
yellowStatus = firebase.get('/yellowLed')

while True:
    # Check each button to determine whether any of them has been pressed. If
    # the OK button is pressed, the program exits the while loop and writes the
    # movement_list to the Firebase database. If any of the directional buttons
    # are pressed, the commands should be stored in the movement_list.

    # Write your code here
    if(redStatus == False):
        GPIO.output(23)=GPIO.HIGH
        time.sleep(0.25)
        redStatus = firebase.get('/redLed')
    elif(redStatus == True):
        GPIO.output(23)=GPIO.LOW
        time.sleep(0.25)
        redStatus = firebase.get('/redLed')
    elif(yellowStatus == False):
        GPIO.output(24)=GPIO.HIGH
        time.sleep(0.25)
        yellowStatus = firebase.get('/yellowLed')
    elif(yellowStatus == True):
        GPIO.output(24)=GPIO.LOW
        time.sleep(0.25)
        yellowStatus = firebase.get('/yellowLed')