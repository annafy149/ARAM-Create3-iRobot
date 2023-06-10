from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth())
speed = 5
Lth = 120
th = 170
map_items = {"apple": [6,15], "soda": [5,10]}

async def check(sensors,num):
    return sensors[num] > 150

async def check2(sensors,num):
    return sensors[num] > 150

async def position(key):
    loc = map_items[key]
    locx = loc[0]
    locy = loc[1]
    return locx,locy

async def cur_pos():
    pos = await robot.get_position()
    return pos.x,pos.y,pos.heading

async def obsi(robot):
    while True:
        sensors = (await robot.get_ir_proximity()).sensors
        if await check(sensors,3):
            await robot.turn_right(90)
            x = await cur_pos()
        if sensors[0] < th and sensors[0] > 0:
            print( "no left wall" )
            await robot.move(23)
            await robot.turn_left(90)
            await robot.move(10)
            await robot.turn_left(90)
        elif sensors[0] >= th:
            print( "left wall" )
            await robot.set_wheel_speeds(10,10)
        if sensors[5] < th and sensors[5] > 0:
            print( "no right wall" )
            await robot.move(23)
            await robot.turn_right(90)
            await robot.move(10)
            await robot.turn_right(90)
        elif sensors[0] >= th:
            print( "right wall" )
            await robot.set_wheel_speeds(10,10)

async def sound(robot):
    for i in range(1, 10):
        await robot.play_note(i*100, 0.25)
    await robot.stop_sound()

async def in_range(target, cur):
    if (target-0.4) < cur < (target+0.4):
        return True
    else:
        return False

async def ret(robot):
    count = 1
    x = 1
    y = 1
    await robot.turn_left(180)
    if_loc = False
    while not if_loc:
        await robot.set_wheel_speeds(10,10)
        pos = await robot.get_position()
        curx = pos.x/100
        cury = pos.y/100
        curhead = pos.heading
        #await obsi(robot)
        print(cury, end = ' ')
        print(curx)
        x_in = await in_range(x,curx)
        y_in = await in_range(y,cury)
        if(x_in and count == 1):
            await robot.turn_left(90)
            count = count - 1
        if(x_in and y_in):
            if_loc = True
            await robot.set_wheel_speeds(0,0)
            await sound(robot)

@event(robot.when_play)
async def play(robot):
    count = 1
    x,y = await position('soda')
    if_loc = False
    while not if_loc:
        await robot.set_wheel_speeds(10,10)
        pos = await robot.get_position()
        curx = pos.x/100
        cury = pos.y/100
        curhead = pos.heading
        #await obsi(robot)
        print(cury, end = ' ')
        print(curx)
        x_in = await in_range(x,curx)
        y_in = await in_range(y,cury)
        if(y_in and count == 1):
            await robot.turn_right(90)
            count = count - 1
        if(x_in and y_in):
            await robot.set_wheel_speeds(0,0)
            await sound(robot)
            if_loc = True
            break
    await ret(robot)

robot.play()
