#!/usr/bin/python
# Class routines for MPRLS Pressure Sensor

import time
import pigpio

class MPRLS:
    def __init__(self, i2c_bus=1, i2c_address=0x18, _offset = 14, tca9548a_num=255, tca9548a_addr=0):
        """Initialize the MPRLS Pressure Sensor"""
        self._i2c_bus = i2c_bus
        self._i2c_address = i2c_address
        self._tca9548a_num = tca9548a_num
        self._tca9548a_addr = tca9548a_addr
        self._i2c = None
        self._temp_offset = _offset
        self._Start1Read = [0xAA, 0x00, 0x00]
        self._pi = pigpio.pi()
        self._pressure = None
    
    def open_port(self, _i2c_bus, _i2c_address):
        # open GPIO port to directly write I2C
        self._i2c = self._pi.i2c_open(self._i2c_bus, self._i2c_address)
        
    def read_pressure(self):
        ret_val = 0
        status = 0
        # Send a wake up command to the sensor.  It will make one reading then switch off
        try:
            self._pi.i2c_write_device(self._i2c, self._Start1Read)
        except pigpio.error:
            ret_val = -100
        # Allow time for the sensor to process the reading
        time.sleep(0.5)
        
        # Read 4 bytes from the sensor. No register of command is required.
        # This must be a "pure" read, so SMBus Block read would not work
        if ret_val == 0:
            try:
                (count, byteArray) = self._pi.i2c_read_device(self._i2c, 4)
            except pigio.error:
                ret_val = -100
            
            if ret_val == 0:
                status = byteArray[0]
                # Check status byte to verify a valid read
                if (status & 1) or (status & 4) or (status & 32):
                    # The sensor has an error
                    ret_val = -100
                elif status == 64:
                    # The sensor is powered up and it was a good read
                    Pressure = (((byteArray[1] * 256) + byteArray[2]) * 256) + byteArray[3]
                    ret_val = (((Pressure - 1677722) * 25) / (15099494 - 1677722) - self._temp_offset)
                    self._pressure = ret_val
        return ret_val
        
    def close_port(self):
        self._pi.i2c_close(self._i2c)
