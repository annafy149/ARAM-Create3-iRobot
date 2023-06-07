import RPi.GPIO as GPIO
from time import sleep
import board
import pyrebase
#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer = 23
restart = True
GPIO.setup(buzzer,GPIO.OUT)
#Run forever loop
i = 0

config = {
  "apiKey": "AgelVv5X3GfyZF06g19M8FW2lXW913HRWehF0LXT",
  "authDomain": "weapondetectiondatabase.firebase.com",
  "databaseURL": "https://weapondetectiondatabase-default-rtdb.firebaseio.com",
  "storageBucket": "weapondetectiondatabase.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

while restart:
    trigger = input()
    if trigger == 'Gun' or trigger == 'gun' or trigger == 'GUN':
        weapon = 'Gun'
        Alert = "Gun fire at Powelton Avenue"
        print("Alert! "+ Alert)
        print()
        data = {
            "Latitude": '-'+'75.191750',
            "Longitute": '39.961025',
            "Weapon": weapon
            }
        db.child("WeaponDetection").child("1-set").set(data)
        db.child("WeaponDetection").child("2-push").push(data)
        print("Send Data to Firebase Using Raspberry Pi")
        print("----------------------------------------")
        print()
        while i <= 15:
            GPIO.output(buzzer,GPIO.HIGH)
            print ("Beep")
            sleep(0.5) # Delay in seconds
            GPIO.output(buzzer,GPIO.LOW)
            print ("No Beep")
            sleep(0.5)
            i = i + 1
        i = 0
    elif trigger == 'Knife' or trigger == 'knife' or trigger == 'KNIFE':
        Alert = "Potential stabbing incident at Powelton Avenue"
        weapon = 'Knife'
        print("Alert! "+ Alert)
        print()
        data = {
            "Latitude": '-'+'75.191750',
            "Longitute": '39.961025',
            "Weapon": weapon
            }
        db.child("WeaponDetection").child("1-set").set(data)
        db.child("WeaponDetection").child("2-push").push(data)
        print("Send Data to Firebase Using Raspberry Pi")
        print("----------------------------------------")
        print()
        while i <= 8:
            GPIO.output(buzzer,GPIO.HIGH)
            print ("Beep")
            sleep(0.67) # Delay in seconds
            GPIO.output(buzzer,GPIO.LOW)
            print ("No Beep")
            sleep(0.33)
            GPIO.output(buzzer,GPIO.HIGH)
            print ("Beep")
            sleep(0.33) # Delay in seconds
            GPIO.output(buzzer,GPIO.LOW)
            print ("No Beep")
            sleep(0.33)
            i = i + 1
        i = 0
    else:
        restart = True
    