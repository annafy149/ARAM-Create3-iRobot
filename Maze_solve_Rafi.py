from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note
#robot = Root(Bluetooth())
robot = Create3(Bluetooth())
speed = 15
status = 'no bump'
bumpcount = 0
x = 0
y = 300
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
    #await robot.turn_left(90)
    #await robot.move(-20)
    #await robot.turn_right(90)
    #await robot.move(25)
    #await robot.set_wheel_speeds(0, 0)
    if bumpcount % 2 != 0:
        await backoff_left(robot)
        bumpcount ++ 1
        status = 'bump'
    else: 
        await backoff_right(robot)
        status = 'bump'

'''@event(robot.when_bumped, [True, False])
async def bumped(robot):
    #await robot.turn_left(90)
    #await robot.move(-20)
    #await robot.turn_right(90)
    #await robot.move(25)
    #await robot.set_wheel_speeds(0, 0)
    await backoff_right(robot)
    status = 'bump'

@event(robot.when_bumped, [False, True])
async def bumped(robot):
    #await robot.turn_left(90)
    #await robot.move(-20)
    #await robot.turn_right(90)
    #await robot.move(25)
    #await robot.set_wheel_speeds(0, 0)
    await backoff_right(robot)
    status = 'bump'
'''
@event(robot.when_play)
async def play(robot):
    await robot.set_wheel_speeds(speed, speed)
    while True:
        if status == 'bump':
            if bumpcount % 2 != 0:
                await backoff_left(robot)
            else: await backoff_right(robot)
            pos = await robot.get_position()
        if status == 'no bump':
            await forward(robot)
            pos = await robot.get_position()
            print(pos.x / 10, pos.y / 10)
            await robot.navigate_to(x, y)
robot.play()

