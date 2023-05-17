from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth())
speed = 5
Lth = 120
th = 150
Rlength = 1.522 #meters

async def check(sensors,num):
    return sensors[num] > 150
@event(robot.when_play)
async def play(robot):
    while True:
        await robot.set_wheel_speeds(10,10)
        sensors = (await robot.get_ir_proximity()).sensors
        print(sensors)
        if await check(sensors,0):
            await robot.turn_left(90)
        if await check(sensors,3):
            await robot.move(-2)
            await robot.turn_left(90)
        if await check (sensors,5):
            await robot.turn_right(90)
robot.play()

# this does make the ir sensors work however it is only basic and can break unexpectidly depending upon what changes were made