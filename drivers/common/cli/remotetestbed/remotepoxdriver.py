#!/usr/bin/env python
'''
Created on 12-Feb-2013

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)

RemoteVMDriver is the basic driver which will handle the Mininet functions
'''

import pexpect
import struct
import fcntl
import os
import signal
import re
import sys
import time

sys.path.append("../")

from drivers.common.cli.remotetestbeddriver import RemoteTestBedDriver

class RemotePoxDriver(RemoteTestBedDriver):
    '''
        RemoteVMDriver is the basic driver which will handle the Mininet functions
    '''
    def __init__(self):
        super(RemoteTestBedDriver, self).__init__()
        
    def connect(self,**connectargs):
        for key in connectargs:
            vars(self)[key] = connectargs[key]
        
        self.name = self.options['name']

        self.handle = super(RemotePoxDriver,self).connect(user_name = self.user_name, ip_address = self.ip_address,port = self.port, pwd = self.pwd)
        if self.handle :
            main.log.info(self.name+" connected successfully ")  
            
            self.execute(cmd="cd "+self.options['pox_lib_location'],prompt="/pox\$",timeout=120)
            self.execute(cmd='./pox.py samples.of_tutorial',prompt="DEBUG:",timeout=120)
            return self.handle
        return main.TRUE
        
    def disconnect(self,handle):
        if self.handle:
            self.execute(cmd="exit()",prompt="/pox\$",timeout=120)
        else :
            main.log.error("Connection failed to the host") 