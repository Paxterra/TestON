#!/usr/bin/env python
'''
Created on 31-May-2013 

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)      

    TestON is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    TestON is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with TestON.  If not, see <http://www.gnu.org/licenses/>.        


''' 
import time
import pexpect
import struct, fcntl, os, sys, signal
import sys
sys.path.append("../")
from drivers.common.clidriver import CLI

class OnosCliDriver(CLI):
    # The common functions for emulator included in ONOS cli
    def __init__(self):
        super(CLI, self).__init__()
        
    def connect(self,**connectargs):
        for key in connectargs:
           vars(self)[key] = connectargs[key]

        
        self.name = self.options['name']

        self.handle = super(OnosCliDriver,self).connect(user_name = self.user_name, ip_address = self.ip_address,port = self.port, pwd = self.pwd)
         
        if self.handle:
            return self.handle
        else :
            return main.FALSE
        
    def start(self):
        self.execute(cmd="\r",prompt="\$",timeout=10)
        self.execute(cmd="~/ONOS/start-onos.sh start",prompt="admin",timeout=10)

    def status(self):
        self.execute(cmd="\r",prompt="\$",timeout=10)
        self.execute(cmd="~/ONOS/start-onos.sh status ",prompt="admin",timeout=10)
        self.execute(cmd="\r",prompt="\$",timeout=10)
    
    def stop(self):
        self.execute(cmd="\r",prompt="\$",timeout=10)
        self.execute(cmd="~/ONOS/start-onos.sh stop ",prompt="admin",timeout=10)
        self.execute(cmd="\r",prompt="\$",timeout=10)
 
    def disconnect(self):
        
        response = ''
        main.log.info("Disconnecting ONOS")
        if self.handle:
            self.execute(cmd = "exit",prompt= "\$",timeout = 10)
        else :
            main.log.error("Connection failed to the host")
            response = main.FALSE
        return response 
