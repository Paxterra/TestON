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

class RemoteVMDriver(RemoteTestBedDriver):
    '''
        RemoteVMDriver is the basic driver which will handle the Mininet functions
    '''
    def __init__(self):
        super(RemoteTestBedDriver, self).__init__()
        
    def connect(self,**connectargs):
        for key in connectargs:
            vars(self)[key] = connectargs[key]
        
        self.name = self.options['name']

        self.handle = super(RemoteVMDriver,self).connect(user_name = self.user_name, ip_address = self.ip_address,port = self.port, pwd = self.pwd)
        if self.handle :
            print "connected "+self.name
            return self.handle