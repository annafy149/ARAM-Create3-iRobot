
from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth())
speed = 15
th = 200


async def forward(robot):
    await robot.set_wheel_speeds(speed, speed)


async def backoff_right(robot):
    await robot.move(-20)
    await robot.turn_right(90)
    await robot.move(40)
    await robot.turn_left(90)

async def backoff_left(robot):
    await robot.move(-20)
    await robot.turn_left(90)
   # await robot.move(100)
   # await robot.turn_right(90)

@event(robot.when_play)
async def play(robot):
    await forward(robot)
    count = 0
    while True:
        sensors = (await robot.get_ir_proximity()).sensors
        if sensors[3] > th and count < 1:
            pos0 = await robot.get_position()
            await backoff_right(robot)
            pos1 = await robot.get_position()
            await forward(robot)
            count += 1

        elif sensors[3] > th and count == 1:
            pos2 = await robot.get_position()
            await backoff_left(robot)
            pos3 = await robot.get_position()
            await forward(robot)
            count += 1

        elif count == 2:
            await robot.navigate_to(50, 140)
            await robot.navigate_to(pos3.x / 10, pos3.y / 10)
            await robot.navigate_to(pos2.x / 10, pos2.y / 10)
            await robot.navigate_to(pos1.x / 10, pos1.y / 10)
            await robot.navigate_to(0, 0)
            count = 0

robot.play()
