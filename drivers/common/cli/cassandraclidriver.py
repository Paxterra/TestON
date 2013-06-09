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


CassandraCliDriver is the basic driver which will handle the Cassandra functions
'''

import pexpect
import struct
import fcntl
import os
import signal
import re
import sys
import core.teston
import time

sys.path.append("../")
from drivers.common.clidriver import CLI

class CassandraCliDriver(CLI):
    '''
        CassandraCliDriver is the basic driver which will handle the Cassandra's functions
    '''
    def __init__(self):
        super(CLI, self).__init__()
        self.handle = self
        self.wrapped = sys.modules[__name__]

    def connect(self, **connectargs):
        # Here the main is the TestON instance after creating all the log handles.
        self.port = None
        for key in connectargs:
            vars(self)[key] = connectargs[key]       
        
        self.name = self.options['name']
        self.handle = super(CassandraCliDriver, self).connect(user_name = self.user_name, ip_address = self.ip_address,port = self.port, pwd = self.pwd)
        
        self.ssh_handle = self.handle
        if self.handle :
            self.start()
            return main.TRUE
        else :
            main.log.error("Connection failed to the host "+self.user_name+"@"+self.ip_address) 
            main.log.error("Failed to connect to the Onos system")
            return main.FALSE
   
 
    def start(self):
        ''' This Function will start the Cassandra'''
        self.execute(cmd="\r",prompt="\$",timeout=10)
        response = self.execute(cmd="~/ONOS/start-cassandra.sh start",prompt="Starting\scassandra(.*)",timeout=10)
        time.sleep(5)
        if re.search("Starting\scassandra(.*)", response):
            main.log.info("Cassandra Started Successfully")
            return main.TRUE
        else:
            main.log.error("Failed to start Cassandra"+ response)
            return main.FALSE
        
    def status(self):
        '''This Function will return the Status of the Cassandra '''
        time.sleep(5)
        self.execute(cmd="\r",prompt="\$",timeout=10)
        response = self.execute(cmd="~/ONOS/start-cassandra.sh status ",prompt="\d+\sinstance\sof\scassandra\srunning(.*)",timeout=10)
        

        self.execute(cmd="\r",prompt="\$",timeout=10)
        return response
        
        if re.search("0\sinstance\sof\scassandra\srunning(.*)") :
            main.log.info("Cassandra not running")
            return main.TRUE
        elif re.search("1\sinstance\sof\scassandra\srunning(.*)"):
            main.log.warn("Cassandra Running")
            return main.TRUE
            
    def stop(self):
        '''This Function will stop the Cassandra if it is Running''' 
        self.execute(cmd="\r",prompt="\$",timeout=10)
        time.sleep(5)
        response = self.execute(cmd="~/ONOS/start-cassandra.sh stop ",prompt="Killed\sexisting\sprosess(.*)",timeout=10)
        self.execute(cmd="\r",prompt="\$",timeout=10)
        if re.search("Killed\sexisting\sprosess(.*)",response):
            main.log.info("Cassandra Stopped")
            return main.TRUE
        else:
            main.log.warn("Cassndra is not Running")
            return main.FALSE
            
    def disconnect(self):
        
        response = ''
        main.log.info("Disconnecting Cassandra")
        if self.handle:
            self.execute(cmd = "exit",prompt= "\$",timeout = 10)
        else :
            main.log.error("Connection failed to the host")
            response = main.FALSE
        return response 
