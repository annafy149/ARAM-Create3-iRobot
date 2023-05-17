

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

#robot = Root(Bluetooth())
robot = Create3(Bluetooth())

speed = 200.0



@event(robot.when_bumped, [True, True])
async def bumped(robot):
    await robot.set_lights_rgb(0, 255, 0)
    await robot.navigate_to(0, 0)



@event(robot.when_play)
async def play(robot):
    print('Hello')
    await robot.set_wheel_speeds(speed, speed)
    print('Bye')


@event(robot.when_play)
async def play(robot):
    print('Bye')


robot.play()
