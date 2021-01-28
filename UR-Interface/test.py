import numpy as np
from Robot.UR.URRobot import URRobot

host = "192.168.178.4"
robot = URRobot(host)
print("Connected to robot")
#robot.movel((-0.3, -1.0, -0.2, 0, -3.14, 0))
tcp=robot.get_tcp_position()

print("TCP intial position is ",tcp)

print("moving Robot")
robot.translate((-0.1, 0.0, 0.0))

print("Robot moved!!")

