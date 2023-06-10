from time import sleep
import board
import pyrebase
from Store_map_simulator import the_path 
restart = True
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
    if trigger == 'Origin':
        print("Back Home!")
        print()
        data = {
            "X datapoint": '-'+'75.191750',
            "Y datapoint": '39.961025',
            "Status": 'charging'
            }
        db.child("ARAM Navigation").child("1-set").set(data)
        db.child("ARAM Navigation").child("2-push").push(data)
        print("Send Data to Firebase Using Mobile app/Kiosk")
        print("----------------------------------------")
        print()

    elif trigger == 'Product':
        print("Destination Reached!")
        print()
        data = {
            "X datapoint": '-'+'75.191750',
            "Y datapoint": '39.961025',
            "Weapon": ''
            }
        db.child("ARAM Navigation").child("1-set").set(data)
        db.child("ARAM Navigation").child("2-push").push(data)
        print("Send Data to Firebase Using Mobile app/Kiosk")
        print("----------------------------------------")
        print()
        
    else:
        restart = True
    