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
import re
sys.path.append("../")
from drivers.common.clidriver import CLI

class OnosCliDriver(CLI):
    
    def __init__(self):
        super(CLI, self).__init__()
        
    def connect(self,**connectargs):
        for key in connectargs:
           vars(self)[key] = connectargs[key]

        
        self.name = self.options['name']
        self.handle = super(OnosCliDriver,self).connect(user_name = self.user_name, ip_address = self.ip_address,port = self.port, pwd = self.pwd)

        if self.handle:
            self.start()
            self.start_rest()
            return self.handle
        else :
            return main.FALSE
        
    def start(self):
        self.execute(cmd="\r",prompt="\$",timeout=10)
        response = self.execute(cmd="~/ONOS/start-onos.sh start",prompt="Starting\sONOS\scontroller",timeout=10)
        time.sleep(5)
        response = response + self.execute(cmd="\r",prompt="\$",timeout=10)
        if re.search("Starting\sONOS\scontroller",response):
            main.log.info("ONOS Started Successfully")
        else :
            main.log.warn("Failed to start ONOS")
    
    def start_rest(self):
        response = self.execute(cmd="~/ONOS/start-rest.sh start",prompt="admin",timeout=10)
        if re.search("admin",response):
            main.log.info("Rest Server Started Successfully")
            time.sleep(5)
            return main.TRUE
        else :
            main.log.warn("Failed to start Rest Server")   
            return main.FALSE     
        
    def status(self):
        self.execute(cmd="\r",prompt="\$",timeout=10)
        response = self.execute(cmd="~/ONOS/start-onos.sh status ",prompt="\d+\sinstance\sof\sonos\srunning",timeout=10)
        self.execute(cmd="\r",prompt="\$",timeout=10)
        if re.search("1\sinstance\sof\sonos\srunning",response):
            main.log.info("ONOS instance Running")
        elif re.search("0\sinstance\sof\sonos\srunning",response):
            main.log.error("ONOS not Running")
        else :
            main.log.error("No Response"+ response)
        return response
    
    def rest_status(self): 
        response = self.execute(cmd="~/ONOS/start-rest.sh status ",prompt="running",timeout=10)
        if re.search("rest\sserver\sis\srunning",response):
            main.log.info("Rest Server is running")
        elif re.search("rest\sserver\sis\snot\srunning",response):
            main.log.warn("Rest Server is not Running")
        else :
            main.log.error("No response" +response)
        self.execute(cmd="\r",prompt="\$",timeout=10)
        
        return response
    
    def stop(self):
        self.execute(cmd="\r",prompt="\$",timeout=10)
        response = self.execute(cmd="~/ONOS/start-onos.sh stop ",prompt="admin",timeout=10)
        self.execute(cmd="\r",prompt="\$",timeout=10)
        
        if re.search("Killed", response):
            main.log.info("ONOS Server Stopped")
            return main.TRUE
        else :
            main.log.error("Failed to Stop, ONOS Server is not Running")
            return main.FALSE
    
    def rest_stop(self):
        response = self.execute(cmd="~/ONOS/start-rest.sh stop ",prompt="killing",timeout=10)
        self.execute(cmd="\r",prompt="\$",timeout=10)
        if re.search("killing", response):
            main.log.info("Rest Server Stopped")
            return main.TRUE
        else :
            main.log.error("Failed to Stop, Rest Server is not Running")
            return main.FALSE
        
    def disconnect(self):
        
        response = ''
        main.log.info("Disconnecting ONOS")
        if self.handle:
            self.execute(cmd = "exit",prompt= "\$",timeout = 10)
        else :
            main.log.error("Connection failed to the host")
            response = main.FALSE
        return response 
