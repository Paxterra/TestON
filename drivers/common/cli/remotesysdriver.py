#!/usr/bin/env python
'''
Created on 26-Oct-2012 

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)      
''' 
import time
import pexpect
import struct, fcntl, os, sys, signal
import sys
sys.path.append("../")
from drivers.common.clidriver import CLI

class RemoteSysDriver(CLI):
    # The common functions for emulator included in emulatordriver
    def __init__(self):
        super(CLI, self).__init__()
        
    def connect(self,**connectargs):
        for key in connectargs:
            vars(self)[key] = connectargs[key]
        
        self.name = self.options['name']

        self.handle = super(RemoteSysDriver,self).connect(user_name = self.user_name, ip_address = self.ip_address,port = self.port, pwd = self.pwd)
        if self.handle:
            self.execute(cmd= "\r",prompt= "\$",timeout= 10)
            self.execute(cmd= "ssh vyatta@192.164.56.81",prompt= "word:",timeout= 10)
            self.execute(cmd = "vyatta",prompt = "\$",timeout = 10)
            self.execute(cmd = "reboot",prompt = "(.*)",timeout = 10)
            
            #self.execute(cmd = "~.",prompt= ".*",timeout= 10)
        return main.TRUE

