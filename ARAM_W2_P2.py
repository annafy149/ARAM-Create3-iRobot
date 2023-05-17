from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note
#robot = Root(Bluetooth())
robot = Create3(Bluetooth())
speed = 25

@event(robot.when_bumped, [True, True])
async def bumped(robot):
    
    await robot.turn_left(90)
    await robot.move(90)
    await robot.turn_right(90)
    #await robot.move(25)
    #await robot.set_wheel_speeds(speed, speed)
    pos = await robot.get_position()
    print(pos.x / 10, pos.y / 10)
    await robot.navigate_to(0, 488)
    await robot.navigate_to(pos.x / 10, pos.y /10)
    await robot.navigate_to(0,-20)
    await robot.navigate_to(pos.x / 10, pos.y / 10)
    await robot.navigate_to(0, 488)

@event(robot.when_play)
async def play(robot):
    await robot.set_wheel_speeds(speed, speed)
    

robot.play()
