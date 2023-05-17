from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note
robot = Create3(Bluetooth())
speed = 12
userChoice = input("select item (1-5): \n\n")
item1 = (125, 125)
item2 = (-125, 125)
item3 = (125, -125)
item4 = (-125, -125)
inventory = {1: item1, 2: item2, 3: item3, 4: item4}
target = inventory[int(userChoice)]
print(target)


#@event(robot.when_play)
#async def play(robot):
#    
