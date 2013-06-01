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


FlowVisorDriver is the basic driver which will handle the Zookeeper functions
'''

import pexpect
import struct
import fcntl
import os
import signal
import re
import sys
import core.teston
sys.path.append("../")
from drivers.common.cli.onosclidriver import OnosCliDriver

class CassandraCliDriver(OnosCliDriver):
    '''
        FlowVisorDriver is the basic driver which will handle the Zookeeper functions
    '''
    def __init__(self):
        super(OnosCliDriver, self).__init__()
        self.handle = self
        self.wrapped = sys.modules[__name__]

    def connect(self, **connectargs):
        #,user_name, ip_address, pwd,options):
        # Here the main is the TestON instance after creating all the log handles.
        self.port = None
        for key in connectargs:
            vars(self)[key] = connectargs[key]       
        
        self.name = self.options['name']
        self.handle = super(CassandraCliDriver, self).connect(user_name = self.user_name, ip_address = self.ip_address,port = self.port, pwd = self.pwd)
        
        self.ssh_handle = self.handle
        
        # Copying the readme file to process the 
        if self.handle :
            
            return main.TRUE
        else :
            main.log.error("Connection failed to the host "+self.user_name+"@"+self.ip_address) 
            main.log.error("Failed to connect to the Onos system")
            return main.FALSE
   
 
    def start(self):
        self.execute(cmd="\r",prompt="\$",timeout=10)
        self.execute(cmd="~/ONOS/start-cassandra.sh start",prompt="admin",timeout=10)

    def status(self):
        self.execute(cmd="\r",prompt="\$",timeout=10)
        self.execute(cmd="~/ONOS/start-cassandra.sh status ",prompt="admin",timeout=10)
        self.execute(cmd="\r",prompt="\$",timeout=10)
    
    def stop(self):
        self.execute(cmd="\r",prompt="\$",timeout=10)
        self.execute(cmd="~/ONOS/start-cassandra.sh stop ",prompt="admin",timeout=10)
        self.execute(cmd="\r",prompt="\$",timeout=10)
 
    def disconnect(self):
        
        response = ''
        main.log.info("Disconnecting Zookeeper")
        if self.handle:
            self.execute(cmd = "exit",prompt= "\$",timeout = 10)
        else :
            main.log.error("Connection failed to the host")
            response = main.FALSE
        return response 
