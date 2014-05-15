#!/usr/bin/python/
'''
Created on 09-MAY-2014
    @author :
       
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
import pexpect
import struct
import fcntl
import os
import signal
import re
import sys
import requests
import json
import httplib
import httplib2
import urllib
from requests.auth import HTTPBasicAuth
import core.teston
sys.path.append("../")
from drivers.common.restapidriver import RESTAPI
class OdlDriver(RESTAPI):
    '''
        OdlCliDriver is the controller driver which will handle the Mininet functions
    '''
    def __init__(self):
        super(RESTAPI, self).__init__()
        self.handle = self
        self.wrapped = sys.modules[__name__]
        self.flag = 0

    def connect(self, **connectargs):
        for key in connectargs:
            vars(self)[key] = connectargs[key] 
        self.name = self.options['name']
        self.handle = super(OdlDriver, self).connect(user_name = self.user_name, ip_address = self.ip_address,port = None, pwd = self.pwd)
        self.ssh_handle = self.handle
	if self.handle :
            main.log.info("Clearing any residual state or processes")
            result = self.execute(cmd="sudo mn -c",timeout=30,prompt="password")
            pattern = '[sudo]'
            if utilities.assert_matches(expect=pattern,actual=result,onpass="password is being asked",onfail="password is not being asked"):
                self.execute(cmd=self.pwd,prompt="\$",timeout=30) 
            else :
                main.log.info("password is not being asked")
                pass
            self.headers={'Content-type': 'application/json', 'Accept': 'application/json'}
            main.log.info("Getting OpenDayLight Controller")
            self.execute(cmd="cd opendaylight",timeout=10,prompt="\$")
            main.log.info("setting JAVA home")
            result = self.execute(cmd="export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-i386",prompt="\$",timeout=10)#Enter Default JDK Package
            main.log.info("Running opendaylight controller")
            result = self.execute(cmd="./run.sh",prompt="Statistics Provider started.",timeout=300)
            result = self.execute(cmd="ss",prompt="Framework is launched.",timeout=10)
            pattern='Framework'
            if utilities.assert_matches(expect=pattern,actual=result,onpass="OpenDayLight Controller is Running",onfail="Failed to run Opendaylight controller"):
            	try :
		    main.log.info("Connecting to topology url")
		    urllib.urlopen(self.options['topology_url'])
		    main.log.info("Connection authentication for restapi")
		    self.auth = HTTPBasicAuth(self.options['username'],self.options['password'])         
            	except Exception,e:
                    main.log.error(e)
            return main.TRUE
        else :
            main.log.info("opendaylight execution is failed")
            self.disconnect()
            return main.FALSE

    def get(self,URL) : 
        try :
            self.request = requests.get(url=URL,auth=self.auth)
            main.log.info(self.request.json())
	    main.log.info(self.request.status_code)
	    main.log.info(self.request.text)
            return self.request.status_code
        except :
            main.log.error("getting topology failed because of"+str(sys.exc_info()[0]))
            main.log.warn("Assertion Failed")
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    def post(self,URL,BODY) : 
        try :
            self.request = requests.post(url=URL,data=BODY,headers=self.headers,auth=self.auth)
            main.log.info(self.request.status_code)
	    main.log.info(self.request.text)
            return self.request.status_code
        except :
            main.log.error("getting topology failed because of"+str(sys.exc_info()[0]))
            main.log.warn("Assertion Failed")
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    def put(self,URL,BODY) : 
        try :
            self.request = requests.put(url=URL,data=BODY,headers=self.headers,auth=self.auth)
	    main.log.info(self.request.status_code)
	    main.log.info(self.request.text)
            return self.request.status_code
        except :
            main.log.error("getting topology failed because of"+str(sys.exc_info()[0]))
            main.log.warn("Assertion Failed")
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    def delete(self,URL) : 
        try :
            self.request = requests.delete(url=URL,headers=self.headers,auth=self.auth)
	    main.log.info(self.request.status_code)
	    main.log.info(self.request.text)
            return self.request.status_code
        except :
            main.log.error("getting topology failed because of"+str(sys.exc_info()[0]))
            main.log.warn("Assertion Failed")
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    def disconnect(self):
        response = ''
        main.log.info("Disconnecting opendaylight")
        if self.handle:
            self.execute(cmd="exit",prompt="(.*)",timeout=120)
            response = self.execute(cmd="y",prompt="(.*)",timeout=120)

        else :
            main.log.error("Failed to disconnect")
            response = main.FALSE
        return response 
             
if __name__ != "__main__":
    import sys
    sys.modules[__name__] = OdlDriver()
