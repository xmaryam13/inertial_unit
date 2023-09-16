from controller import Robot
import math
from controller import Keyboard

# create the Robot instance.
robot = Robot()
keyboard = Keyboard()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

wheel_motor1 = robot.getDevice('motor1')
wheel_motor1.setPosition(float('inf'))
wheel_motor1.setVelocity(0.0)

wheel_motor2 = robot.getDevice('motor2')
wheel_motor2.setPosition(float('inf'))
wheel_motor2.setVelocity(0.0)

wheel_motor3 = robot.getDevice('motor3')
wheel_motor3.setPosition(float('inf'))
wheel_motor3.setVelocity(0.0)

wheel_motor4 = robot.getDevice('motor4')
wheel_motor4.setPosition(float('inf'))
wheel_motor4.setVelocity(0.0)

speed=5

# initialize the InertialUnit
imu = robot.getDevice('inertial unit')
imu.enable(timestep)

keyboard.enable(timestep)

def move(left_speed,right_speed):
    wheel_motor1.setVelocity(right_speed)
    wheel_motor2.setVelocity(right_speed)  
    wheel_motor3.setVelocity(left_speed)
    wheel_motor4.setVelocity(left_speed)  
            
while robot.step(timestep) != -1:

    # fetch the orientation of the robot using InertialUnit and log it
    angle = imu.getRollPitchYaw()
    
    yaw_current = round(math.degrees(angle[2]))+180
    print("Currently facing towards "+ str(yaw_current)+" degrees")
    
    key_pressed= keyboard.getKey()
    
    if(key_pressed== 315):
        move(5,5)
        
    if(key_pressed== 317):
        move(-5,-5)
          
    if(key_pressed== 314):
        move(-5,5)
        
    if(key_pressed== 316):
        move(5,-5)
        
    if(key_pressed== -1):
        move(0,0)