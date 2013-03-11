#!/usr/bin/env python
'''
Created on 12-Feb-2013

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)

HPSwitchDriver is the basic driver which will handle the Mininet functions
'''

import pexpect
import struct
import fcntl
import os
import signal
import re
import sys
import time
import core.ofautomation
sys.path.append("../")
from drivers.common.clidriver import CLI

class HPSwitchDriver(CLI):
    '''
        HPSwitchDriver is the basic driver which will handle the Mininet functions
    '''
    def __init__(self):
        super(CLI, self).__init__()
        
    def connect(self,**connectargs):
        for key in connectargs:
            vars(self)[key] = connectargs[key]
        
        self.name = self.options['name']

        self.handle = super(HPSwitchDriver,self).connect(user_name = self.user_name, ip_address = self.ip_address,port = self.port, pwd = self.pwd)
    