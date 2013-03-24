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

class RemoteTestBedDriver(CLI):
    # The common functions for emulator included in RemoteTestBedDriver
    def __init__(self):
        super(CLI, self).__init__()
        
    def connect(self,**connectargs):
        for key in connectargs:
           vars(self)['vm_'+key] = connectargs[key]

        remote_user_name = main.componentDictionary[self.name]['remote_user_name']
        remote_ip_address = main.componentDictionary[self.name]['remote_ip_address']
        remote_port = main.componentDictionary[self.name]['remote_port'] 
        remote_pwd = main.componentDictionary[self.name]['remote_pwd']
        
        self.handle = super(RemoteTestBedDriver,self).connect(user_name = remote_user_name, 
                                                              ip_address = remote_ip_address,
                                                              port = remote_port, pwd = remote_pwd)
        
        if self.handle:
            self.execute(cmd= "\r",prompt= "\$|>|#",timeout= 10)
            self.execute(cmd= "SET CYGWIN=notty",prompt= "\$|>|#",timeout= 10)
            self.execute(cmd= "\r",prompt= "\$|>|#",timeout= 10)
            main.log.info("ssh "+self.vm_user_name+'@'+self.vm_ip_address)
            self.execute(cmd= "ssh "+self.vm_user_name+'@'+self.vm_ip_address,prompt= "(.*)",timeout= 10)
            self.execute(cmd= "\r",prompt= "assword:",timeout= 10)
            self.execute(cmd = self.vm_pwd,prompt = "\$",timeout = 10)
            
            return self.handle
        else :
            return main.FALSE