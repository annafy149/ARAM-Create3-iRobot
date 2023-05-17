from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note
robot = Create3(Bluetooth())
speed = 12
#userChoice = input("select item (1-5): \n\n")
userChoice = 1
box_dimension = a = 200
item1 = (a, a)
item2 = (-a, a)
item3 = (a, -a)
item4 = (-a, -a)
inventory = {1: item1, 2: item2, 3: item3, 4: item4}
target = inventory[int(userChoice)]

async def check(sensors,num):
    return sensors[num] > 150

@event(robot.when_bumped,[])
async def bumped_robot():
    robot.stop()

@event(robot.when_play)
async def play(robot):
    for i in inventory:
        await robot.navigate_to(inventory[i][0], inventory[i][1])
        sensors = (await robot.get_ir_proximity()).sensors
        print(sensors)
        if await check(sensors,0):
            await robot.turn_right(90)
        if await check(sensors,3):
            await robot.move(-2)
            await robot.turn_left(90)
        if await check (sensors,5):
            await robot.turn_left(90)

robot.play()