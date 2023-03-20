#!/usr/bin/python

import smbus

class TCA9845A:
    def __init__(self, bus = 1, address=0x70, ):
        self.i2c_address = address
        self.i2c_bus = bus
        self.bus = smbus.SMBus(self.i2c_bus)
        
    def setup(self, channel):
        try:
            self.bus.write_byte(self.i2c_address, channel)
            return 1
        except Exception as msg:
            return 0, "Fail: {}".format(msg)
    
    def read(self):
        #time.sleep(0.1)
        return self.bus.read_byte(self.i2c_address)
