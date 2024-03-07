import main

import rtde_receive
actual_q = rtde_r.getActualQ()
print(actual_q)




try:
    while True:
        t_start = rtde_c.initPeriod()
        servo_target = getCircleTarget(actual_tcp_pose, time_counter)
        rtde_c.servoL(servo_target, vel, acc, dt, lookahead_time, gain)
        rtde_c.waitPeriod(t_start)
        time_counter += dt

except KeyboardInterrupt:
    print("Control Interrupted!")
    rtde_c.servoStop()
    rtde_c.stopScript()