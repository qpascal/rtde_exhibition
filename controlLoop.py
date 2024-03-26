from rtde_control import RTDEControlInterface as RTDEControl
from rtde_receive import RTDEReceiveInterface as RTDEReceive
import datetime
import math
import os
import psutil
import sys
import time

import pygame

# Function to gather data from robot
def robotData(rtde_r):
    # Get the actual joint positions
    actualQ = rtde_r.getActualQ()
    # Get the actual TCP force
    actualTCPForce = rtde_r.getActualTCPForce()
    # Get the actual TCP speed
    actualTCPSpeed = rtde_r.getActualTCPSpeed()
    # get the actual current
    actualCurrent = rtde_r.getActualCurrent()
    print("Actual joint positions:", actualQ, "\n Actual TCP Force:", actualTCPForce, "\n Actual TCP Speed:", actualTCPSpeed, "\n Actual current inside the robot:", actualCurrent)

# Parameters
vel = 0.5
acc = 0.5
rtde_frequency = 500.0
dt = 1.0/rtde_frequency  # 2ms
flags = RTDEControl.FLAG_VERBOSE | RTDEControl.FLAG_UPLOAD_SCRIPT
ur_cap_port = 50002
robot_ip = "10.211.56.10"
lookahead_time = 0.1
gain = 600
# ur_rtde realtime priorities
rt_receive_priority = 90
rt_control_priority = 85

# Check connection with robot
rtde_r = RTDEReceive(robot_ip, rtde_frequency, [], True, False, rt_receive_priority)
rtde_c = RTDEControl(robot_ip, rtde_frequency, flags, ur_cap_port, rt_control_priority)
# Set application real-time priority
os_used = sys.platform
process = psutil.Process(os.getpid())
if os_used == "win32":  # Windows (either 32-bit or 64-bit)
    process.nice(psutil.REALTIME_PRIORITY_CLASS)
elif os_used == "linux":  # linux
    rt_app_priority = 80
    param = os.sched_param(rt_app_priority)
    try:
        os.sched_setscheduler(0, os.SCHED_FIFO, param)
    except OSError:
        print("Failed to set real-time process scheduler to %u, priority %u" % (os.SCHED_FIFO, rt_app_priority))
    else:
        print("Process real-time priority set to: %u" % rt_app_priority)

time_counter = 0.0

# Attribution of positions
homeJoints = [0.11096344143152237, -1.1199520269977015, -2.5396979490863245, -0.09851295152773076, 1.4749480485916138, 0.31134793162345886]
homePose = rtde_c.getForwardKinematics(homeJoints,rtde_c.getTCPOffset())

XPosLimitPose = [0.05,0,0,0,0,0]
XNegLimitPose = [-0.05,0,0,0,0,0]
YPosLimitPose = [0,0,0.05,0,0,0]
YNegLimitPose = [0,0,-0.05,0,0,0]

# Control parameters
keepPiloting = True
busy = False
verbose = False
targetPose = []

# Go to home position in moveJ
rtde_c.moveJ(homeJoints, vel, acc)

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Game Loop
while keepPiloting :
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            keepPiloting = False
            rtde_c.servoStop()
        elif(event.type == pygame.KEYDOWN and not busy):
            if(event.key == pygame.K_SPACE):
                keepPiloting = False
                rtde_c.servoStop()
            elif(event.key in [pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT]):
                if(event.key == pygame.K_UP):
                    targetPose = rtde_c.poseTrans(XPosLimitPose,rtde_r.getActualTCPPose())
                elif(event.key == pygame.K_DOWN):
                    targetPose = rtde_c.poseTrans(XNegLimitPose,rtde_r.getActualTCPPose())
                elif(event.key == pygame.K_RIGHT):
                    targetPose = rtde_c.poseTrans(YNegLimitPose,rtde_r.getActualTCPPose())
                else:
                    targetPose = rtde_c.poseTrans(YPosLimitPose,rtde_r.getActualTCPPose())
                if rtde_c.isPoseWithinSafetyLimits(targetPose) :
                    t_start = rtde_c.initPeriod()
                    rtde_c.servoL(targetPose, vel, acc, dt, lookahead_time, gain)
                    rtde_c.waitPeriod(t_start)
                    busy = True
        elif(event.type == pygame.KEYUP):
            rtde_c.servoStop()
            busy = False
        if verbose :
            robotData(rtde_r)
    pygame.display.update()


pygame.quit()
time.sleep(2)
rtde_c.moveL(rtde_c.getForwardKinematics(homeJoints,rtde_c.getTCPOffset()),vel,acc,False)

# End connection with robot
print("Control Interrupted!")
rtde_c.servoStop()
rtde_c.stopScript()