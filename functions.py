# Function to connect robot
def connectRobot():
    return "RTDE established"


# Function to disconnect robot
def disconnectRobot(rtde_c):
    rtde_c.stopScript()
    return "Control Interrupted"


# Function to move robot in servoL mode
def moveLRobot():
    x = 0
    return x


# Function to move robot in servoJ mode
def moveJRobot():
    x = 0
    return x


# Function to get data from the robot
def getDataRobot(rtde_r):
    # Actual joint positions
    rtde_r.getActualQ()
    # Actual joint velocities
    rtde_r.getActualQD()
    # Actual joint currents
    rtde_r.getActualCurrent()
    # Actual current window
    rtde_r.getActualCurrentWindow()
    # Joint control currents
    rtde_r.getJointControlOutput()
    # Actual Cartesian coordinates of the tool
    rtde_r.getActualTCPPose()
    # Actual speed of the tool given in Cartesian coordinates [m/s] and [rad/s]
    rtde_r.getActualTCPSpeed()
    # Generalized forces in the TCP
    rtde_r.getActualTCPForce()
    # Tool x, y and z accelerometer values
    rtde_r.getActualToolAccelerometer()
    # Norm of Cartesian linear momentum
    rtde_r.getActualMomentum()
    # Actual joint voltages
    rtde_r.getActualJointVoltage()
    # Program state
    rtde_r.getRuntimeState()
    # Tool output voltage [V]
    rtde_r.getToolOutputVoltage()
    # Tool current [mA]
    rtde_r.getToolOutputCurrent()
    # TCP force scalar [N]
    rtde_r.getTCPForceScalar()
    # Payload mass Kg
    rtde_r.getPayload()
    # Payload Center of Gravity (CoGx, Cogy, CoGz) m
    rtde_r.getPayloadCog()
    # Payload inertia matrix elements [lxx,lyy,lzz,lxy,lxz,lyz] expressed in kg*m^2
    rtde_r.getPayloadInertia()
    # Joint Temperatures
    rtde_r.getJointTemperatures()
    return "Data Stored"


# Function for data display
def dataDisplay():
    return "Data have been displayed"


# Function for RoboDK API feedback loop
def robodkAPIFeedback():
    return "Feedback done to RoboDK API"