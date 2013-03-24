#!/usr/bin/env python
'''
Created on 12-Feb-2013

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)

FloodLightCliDriver is the basic driver which will handle the Mininet functions
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

class FloodLightCliDriver(RemoteTestBedDriver):
    '''
        FloodLightCliDriver is the basic driver which will handle the Mininet functions
    '''
    def __init__(self):
        super(RemoteTestBedDriver, self).__init__()
        
    def connect(self,**connectargs):
        for key in connectargs:
            vars(self)[key] = connectargs[key]
        
        self.name = self.options['name']

        self.handle = super(FloodLightCliDriver,self).connect(user_name = self.user_name, ip_address = self.ip_address,port = self.port, pwd = self.pwd)
        if self.handle :
            main.log.info("Connected "+self.name)
            self.execute(cmd="\r",prompt="\$",timeout=10)
            self.execute(cmd="cd /home/openflow/floodlight/",prompt="floodlight\$",timeout=3)
            self.execute(cmd="java -jar target/floodlight.jar &",prompt="\$",timeout=3)
            self.execute(cmd="\r",prompt="\$",timeout=10)
            return self.handle
        else :
            return main.FALSE