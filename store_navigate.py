from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

#robot = Root(Bluetooth())
Product_loc_x = {"Origin": 0, "Product1": -140, "Product2": 0, "Product3": 140}
Product_loc_y = {"Origin": 0, "Product1": 280, "Product2": 280, "Product3": 280}

finalx = Product_loc_x.get('Product1')
finaly = Product_loc_y.get('Product1')

robot = Create3(Bluetooth())
speed = 15
time = 0.3
th = 200
status = 'no bump'

config = {
  "apiKey": "AgelVv5X3GfyZF06g19M8FW2lXW913HRWehF0LXT",
  "authDomain": "weapondetectiondatabase.firebase.com",
  "databaseURL": "https://ARAMRobotdatabase-default-rtdb.firebaseio.com",
  "storageBucket": "weapondetectiondatabase.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

async def forward(robot):
    await robot.set_wheel_speeds(speed, speed)

async def backoff_right(robot):
    await robot.move(-10)
    await robot.turn_right(90)
    await robot.move(5)
    #await robot.turn_left(90)

async def backoff_left(robot):
    await robot.move(-10)
    await robot.turn_left(90)
    await robot.move(5)
    #await robot.turn_right(90)

@event(robot.when_play)
async def play(robot):
    await forward(robot)
    count = 0
    while True:
        await robot.set_lights_rgb(0, 120.4, 0)
        sensors = (await robot.get_ir_proximity()).sensors
        if sensors[3] > th and count < 1:

            await backoff_right(robot)
            pos0 = await robot.get_position()
            await forward(robot)
            count += 1

        elif sensors[3] > th and count == 1:
            
            await backoff_right(robot)
            pos1 = await robot.get_position()
            await forward(robot)
            count += 1

        elif sensors[3] > th and count == 2:
            
            await backoff_right(robot)
            pos2 = await robot.get_position()
            await forward(robot)
            count += 1

        elif sensors[3] > th and count == 3:
            
            await backoff_left(robot)
            pos3 = await robot.get_position()
            await forward(robot)
            count += 1

        elif sensors[3] > th and count == 4:
            
            await backoff_right(robot)
            pos4 = await robot.get_position()
            await forward(robot)
            count += 1

        elif count == 5: 
            await robot.navigate_to(0, 0)
            await robot.turn_right(45)
            await robot.turn_left(90)
            await robot.turn_right(45)
            await robot.wait(time)
            await robot.navigate_to(pos4.x / 10, pos4.y / 10)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.wait(time)
            await robot.navigate_to(pos3.x / 10, pos3.y / 10)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.wait(time)
            await robot.navigate_to(pos2.x / 10, pos2.y / 10)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.wait(time)
            await robot.navigate_to(pos1.x / 10, pos1.y / 10)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.turn_right(90)
            await robot.wait(time)
            await robot.navigate_to(0, 0)
            await robot.turn_right(45)
            await robot.turn_left(90)
            await robot.turn_right(45)
            await robot.wait(time)
            count = 0

robot.play()
