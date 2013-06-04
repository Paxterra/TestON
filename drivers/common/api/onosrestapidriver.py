#!/usr/bin/env python
'''
Created on 4-Jun-2013

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


onosrestapidriver is the basic driver which will handle the fvtapidriver functions
'''

import pexpect
import struct
import fcntl
import os
import signal
import re
import sys
sys.path.append("../")
from drivers.common.apidriver import API
import urllib
import __builtin__


class OnosRestApiDriver(API):

    def __init__(self):
        super(API, self).__init__()
        print 'init'
                                                

    def connect(self,**connectargs):
        for key in connectargs:
            vars(self)[key] = connectargs[key]
        
        self.name = self.options['name']
        
        connect_result = super(OnosRestApiDriver,self).connect()
        
        ssh_newkey = 'Are you sure you want to continue connecting'
        refused = "ssh: connect to host "+self.ip_address+" port 22: Connection refused"
        if self.port:
            self.handle =pexpect.spawn('ssh -p '+self.port+' '+self.user_name+'@'+self.ip_address,maxread=50000)
        else :
            self.handle =pexpect.spawn('ssh -X '+self.user_name+'@'+self.ip_address,maxread=50000)
            
        self.handle.logfile = self.logfile_handler
        i=self.handle.expect([ssh_newkey,'password:',pexpect.EOF,pexpect.TIMEOUT,refused],120)
        
        if i==0:    
            main.log.info("ssh key confirmation received, send yes")
            self.handle.sendline('yes')
            i=self.handle.expect([ssh_newkey,'password:',pexpect.EOF])
        if i==1:
            main.log.info("ssh connection asked for password, gave password")
            self.handle.sendline(self.pwd)
            self.handle.expect('>|#|$')
            
        elif i==2:
            main.log.error("Connection timeout")
            return main.FALSE
        elif i==3: #timeout
            main.log.error("No route to the Host "+self.user_name+"@"+self.ip_address)
            return main.FALSE
        elif i==4:
            main.log.error("ssh: connect to host "+self.ip_address+" port 22: Connection refused")
            return main.FALSE
    
        
        self.logFileName = main.logdir+"/"+self.name+".session"
        
        if self.handle:
            return self.handle
        else :
            return main.FALSE

    def curlRequest(self):
        try :
            resonse_lines = urllib.urlopen(self.options['topology_url']).readlines()
            print resonse_lines  
            return resonse_lines
        except Exception,e:
           main.log.error(e)
           return "url error"  
   
    def disconnect(self,handle):
        response = ''
        '''
        if self.handle:
            self.handle = handle
            response = self.execute(cmd="exit",prompt="(.*)",timeout=120)
        else :
            main.log.error("Connection failed to the host")
            response = main.FALSE
        '''
        return response  
    
    
   
    
