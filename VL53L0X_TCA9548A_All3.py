

# MIT License
# 
# Copyright (c) 2017 John Bryan Moore
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import VL53L0X
import MCP9808
import TCA9845A
import MPRLS
import sys

i2c_bus = 1
MCP_Address = 0x19      # MCP9808 Sensor I2C Address
MPR_Address = 0x18      # MPR Pressure Sensor I2C Address
VL53L0X_Address = 0x29

Num_Kegs = 3
Keg_Temp = []            # List to hold Temp Sensor Objects
Keg_Press = []           # List to hold Pressure Sensor objects
Keg_Level = []           # List to hold Keg Level sensor objects
Avg_Level = 0
Pressure_Offset = 14.00

###### Start of program


# Create an object for the multiplexer
multiplexer = TCA9845A.TCA9845A( 1, 0x70)

# Sequence through the channels and create objects for each keg sensor
for keg in range(Num_Kegs):
    print(multiplexer.setup(keg+1))
    if multiplexer.setup(keg + 1)==1:
        read_response = multiplexer.read()
        print("TCA9845A I2C channel status: {} (channel {})".format(bin(read_response), read_response))
    
        # Create a Keg Pressure Sensor object for this keg
        Keg_Press.append(MPRLS.MPRLS(i2c_bus, MPR_Address, Pressure_Offset, keg + 1, 0x70))

        # Create a Keg Temperature Sensor for this Keg
        Keg_Temp.append(MCP9808.MCP9808(i2c_bus, MCP_Address, keg + 1, 0x70))
    
        # Create a Keg Level Sensor object for this keg
        Keg_Level.append(VL53L0X.VL53L0X(i2c_bus, VL53L0X_Address))
    else:
        print("Multiplexer setup failed for Channel:", keg)
        sys.exit()

#multiplexer.setup(1)
#read_response = multiplexer.read()
#print("TCA9845A I2C channel status: {} (channel {})".format(bin(read_response), read_response))

Keg_Press[0].open_port(Keg_Press[0]._i2c_bus, Keg_Press[0]._i2c_address)
Keg_Temp[0].open()

# Configure MCP9808 Temperature Sensor
# Set startup mode as continuous conversion
Keg_Temp[0].config(Keg_Temp[0].REG_CONFIG, MCP9808.DeviceMode.Continuous_Conversion)

# Set resolution to .25 deg
Keg_Temp[0].config(Keg_Temp[0].REG_RESOLUTION, MCP9808.Resolution.QuarterDeg)

Keg_Level[0].open()

# Start ranging on TCA9548A bus 1
Keg_Level[0].start_ranging(VL53L0X.Vl53l0xAccuracyMode.BEST)

timing = Keg_Level[0].get_timing()
if timing < 20000:
    timing = 20000
print("Timing %d ms" % (timing/1000))




for count in range(1, 2):
    # Get distance from VL53L0X on TCA9548A bus 1
    distance = Keg_Level[0].get_distance()
    if distance > 0:
        Avg_Level += distance
        print("1: %d mm, %d cm, %d, %d" % (distance, (distance/10), count, Avg_Level/count))
        
    # Get Temp from MCP9808 Sensor
    tempC = Keg_Temp[0].get_temp_C()
    tempF = tempC * 1.8 + 32
    print (" Temperature = :%.2f C or :%.2f F" % (tempC, tempF))
    
    # Get pressure from MPR Sensor
    # This sensor turns on and takes a reading, converts the data, then turns itself back off
    pressure = Keg_Press[0].read_pressure()
    print ("Pressure = :%.2f " % (pressure))

    time.sleep(timing/80000.00)
    
    if count == 20:
        Keg_Temp[0].config(Keg_Temp[0].REG_CONFIG, MCP9808.DeviceMode.Shutdown_Mode)

# End of program.  Stop ranging and close sensors
Keg_Level[0].stop_ranging()
time.sleep(0.5)
Keg_Level[0].close()
time.sleep(0.5)
Keg_Level.clear()

#Close pressure sensor and clear object
Keg_Press[0].close_port()
Keg_Press.clear()

# Close Temperature sensor and clear object
Keg_Temp[0].close()
Keg_Temp.clear()
