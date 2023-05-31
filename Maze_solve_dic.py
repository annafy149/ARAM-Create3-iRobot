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
status = 'no bump'
async def forward(robot):
    await robot.set_wheel_speeds(speed, speed)

async def backoff_right(robot):
    await robot.move(-15)
    await robot.turn_right(90)
    await robot.move(20)
    await robot.turn_left(90)

async def backoff_left(robot):
    await robot.move(-15)
    await robot.turn_left(90)
    await robot.move(20)
    await robot.turn_right(90)

@event(robot.when_bumped, [True, True])
async def bumped(robot):
    await backoff_left(robot)
    status = 'bump'

@event(robot.when_play)
async def play(robot):
    await robot.set_wheel_speeds(speed, speed)
    while True:
        
        if status == 'bump':
            await backoff_left(robot)

        if status == 'no bump':
            await forward(robot)
            pos = await robot.get_position()
            print(pos.x / 10, pos.y / 10)
            await robot.navigate_to(finalx, finaly)

robot.play()

