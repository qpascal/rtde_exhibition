from rtde_control import RTDEControlInterface as RTDEControl
from rtde_receive import RTDEReceiveInterface as RTDEReceive
import datetime
import math
import os
import psutil
import sys


# Parameters
vel = 0.5
acc = 0.5
rtde_frequency = 500.0
dt = 1.0/rtde_frequency  # 2ms
flags = RTDEControl.FLAG_VERBOSE | RTDEControl.FLAG_UPLOAD_SCRIPT
ur_cap_port = 50002
robot_ip = "10.181.128.10"

lookahead_time = 0.1
gain = 600

# ur_rtde realtime priorities
rt_receive_priority = 90
rt_control_priority = 85

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

# Home position
home_tcp_pose = [0.7596026466901262, -0.11484245580840405, 0.31243188874992633, -1.014187171041334, 1.3088531041376177, -1.071596229917346]
rtde_c.moveL(home_tcp_pose, vel, acc)


# Move to init position using moveL
actual_tcp_pose = rtde_r.getActualTCPPose()
print(actual_tcp_pose)


print("Control Interrupted!")
rtde_c.servoStop()
rtde_c.stopScript()
