#declarations
from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note
robot = Create3(Bluetooth())

#prereq variables
userChoice = 1
box_dimension = a = 100
speed = 12
i = 1

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
@event(robot.when_bumped,[True, True])
async def bumped_robot():
    await robot.stop()
    await robot.turn_right(90)
    await robot.move(50)
    while i <= len(inventory):
        #navigates to the inv item from dictionary
        await robot.navigate_to(inventory[i][0], inventory[i][1])
        i ++ 1

#main code 
@event(robot.when_play)
async def play(robot):
    #test case to go through each inv item
    while i <= len(inventory):
        #navigates to the inv item from dictionary
        await robot.navigate_to(inventory[i][0], inventory[i][1])
        i ++ 1

robot.play()