#!/usr/bin/python

# MIT License
#
# Copyright (c) 2021 by Andy McClure
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
import smbus

class Resolution:
    HalfDeg = [0x00]        # +0.5C (tconv = 30ms typ)
    QuarterDeg = [0x01]     # +0.25C (tconv = 65ms typ)
    EighthDeg = [0x10]      # +0.125C (tconv = 130ms typ)
    SixteenthDeg= [0x11]    # +0.0625C (tconv = 250ms typ - Power up Default)
    
class DeviceMode:
    Continuous_Conversion = [0x00, 0x00]
    Shutdown_Mode = [0x01, 0x00]


class MCP9808:
#    """MCP9808."""
    def __init__(self, i2c_bus=1, i2c_address=0x18, tca9548a_num=255, tca9548a_addr=0):
        """Initialize the 9808 Temperature Sensor"""
        self._i2c_bus = i2c_bus
        self._i2c_address = i2c_address
        self._tca9548a_num = tca9548a_num
        self._tca9548a_addr = tca9548a_addr
        self._i2c = smbus.SMBus(i2c_bus)
        self._tempc = None
        # Register Addresses
        self.REG_CONFIG = 0x01       # Configuration Register
        self.REG_T_UPPER = 0x02      # Upper Boundary Temp Register
        self.REG_T_LOWER = 0x03      # Lower Boundary Temp Register
        self.REG_T_CRIT = 0x04       # Critical Temperature Temp Register
        self.REG_T_AMBIENT = 0x05    # Ambient Temerature Register
        self.REG_RESOLUTION = 0x08   # Temp Resolution Register

# Configure MCP9808 chip.
    def config(self, _Register, _data):
        ret_val = 0
  
        # Determine amount of data to be written
        if len(_data) == 2:
            # if more than one byte is to be written, use the i2c Block Write method
            try:
                self._i2c.write_i2c_block_data(self._i2c_address, _Register, _data)
            except IOError:
                ret_val = -1
            
        elif len(_data) == 1:
            try:
                self._i2c.write_byte_data(self._i2c_address, _Register, _data[0])
            except IOError:
                ret_val = -1
        time.sleep(0.1)
        return ret_val
        
    # Get the current temperature from the MCP9808 sensor    
    def get_temp_C(self):
        ret_val = 0
        
        # Get the current data from the ambient temperature registers
        try:
            data = self._i2c.read_i2c_block_data(self._i2c_address, self.REG_T_AMBIENT, 2)
        except IOError:
            data = -99
        if data == -1 or data == -99:
            # Invalid data or read error
            ret_val = -99
        else:
            # Mask off top 3 bits of upper byte, shift it by 8 bits and add the lower byte
            ctemp = ((data[0] & 0x1F) * 256) + data[1]
            
            # Convert the data to Celsius
            if ctemp > 4095:
                # The sign bit (bit 12) was set. This is a negative number
                ctemp -= 8192
            ctemp = ctemp * 0.0625
            ret_val = ctemp
            self._tempC = ctemp
        return ret_val

    def open(self):
        self._i2c.open(bus=self._i2c_bus)
    
    def close(self):
        self._i2c.close()
        self._dev = None

 