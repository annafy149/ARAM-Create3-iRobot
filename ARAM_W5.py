from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth())
speed = 12
th = 250
marks_X = []
marks_Y = []
left = 0
right = 0

async def forward(robot):
    await robot.set_wheel_speeds(speed, speed)


async def backoff_right(robot):
    await robot.move(-5)
    await robot.turn_right(90)
    await robot.move(20)

async def backoff_left(robot):
    await robot.move(-5)
    await robot.turn_left(90)
    await robot.move(20)


@event(robot.when_play)
async def play(robot):
    pos = await robot.get_position()
    marks_X.append(pos.x/10)
    marks_Y.append(pos.y/10)
    await forward(robot)
    while True:
        sensors = (await robot.get_ir_proximity()).sensors
        print(sensors)
        
        if (sensors[3] > th):
            pos = await robot.get_position()
            await backoff_right(robot)
            marks_X.append(pos.x/10)
            marks_Y.append(pos.y/10)
            await forward(robot)

        elif sensors[3] < th and sensors[6] > th and sensors[0] < th:
            await forward(robot)
            left = 1
        
        elif sensors[3] < th and sensors[6] < th and sensors[0] < th and left == 1:
            await robot.move(10)
            await robot.turn_left(90)
            pos = await robot.get_position()
            marks_X.append(pos.x/10)
            marks_Y.append(pos.y/10)
            await forward(robot)

        elif sensors[3] < th and sensors[6] < th and sensors[0] > th:
            await forward(robot)
            right = 1
        
        elif sensors[3] < th and sensors[6] < th and sensors[0] < th and right == 1:
            await robot.move(10)
            await robot.turn_right(90)
            pos = await robot.get_position()
            marks_X.append(pos.x/10)
            marks_Y.append(pos.y/10)
            await forward(robot)
        
        elif (pos.y/10) > 200 and sensors[3] < th and sensors[6] < th and sensors[0] < th:
            await robot.navigate_to(pos.x/10, 305)
            await robot.navigate_to(0, 305)
            marks_X.reverse()
            marks_Y.reverse()
            for i in len(marks_X):
                await robot.navigate_to(marks_X[i], marks_Y[i])
            await robot.set_wheel_speeds(0,0)

        else:
            await forward(robot)

robot.play()
