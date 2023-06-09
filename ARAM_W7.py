from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note
robot = Create3(Bluetooth())
speed = 12
#userChoice = input("select item (1-5): \n\n")
#input is not supported with irobot


#prereq variables
userChoice = 1
box_dimension = a = 100

#set up coordinates for the box
item1 = (a, a)
item2 = (-a, a)
item3 = (a, -a)
item4 = (-a, -a)
#dictionary of item names and their locations
inventory = {1: item1, 2: item2, 3: item3, 4: item4}
target = inventory[int(userChoice)]

#checks if robot is a certain distance from wall
#unused
async def check(sensors,num):
    return sensors[num] > 150

#stops robot when bumped
#unused
@event(robot.when_bumped, [True, True])
async def bumped(robot):
    await robot.turn_left(90)
    await robot.move(25)
    await robot.turn_right(90)
    await robot.move(25)



#main code 
@event(robot.when_play)
async def play(robot):
    await robot.set_wheel_speeds(speed, speed)
    #test case to go through each inv item
    #for i in inventory:
        #navigates to the inv item from dictionary
        #await robot.navigate_to(inventory[i][0], inventory[i][1])
        #initializes sensor check
        #sensors = (await robot.get_ir_proximity()).sensors
        #not breaking the navigate command, doing weird turns at the corners
        #only checking once for each sensor
        #print(sensors)
        #if await check(sensors,0):
        #    await robot.turn_right(90)
        #if await check(sensors,3):
        #    await robot.move(-2)
         #   await robot.turn_left(90)
        #if await check (sensors,5):
        #    await robot.turn_left(90)

robot.play()