 #!/usr/bin/env python
 '''
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
    
Basic Spirent stcdriver which will handle all basic stcdriver functions.
'''
import pexpect
import struct
import fcntl
import os
import signal
import re
import sys
import csv
import core.teston
sys.path.append("../")
from common.apidriver import API
sys.path.append(path+"lib/spirent/API/Python/")
#global STC_PRIVATE_INSTALL_DIR
#STC_PRIVATE_INSTALL_DIR="/home/paxterra/TestON/lib/spirent/"
from StcPython import StcPython
class StcDriver(API):
   
    def __init__(self):
        #super(API, self).__init__()
        self.handle = StcPython()
        main.log.info("STC component initialized")

    def connect(self,**connectargs):
        for key in connectargs:
            vars(self)[key] = connectargs[key]

        self.name = self.options['name']
        main.log.info("Component name is "+self.name)
        connect_result = super(API,self).connect()
        main.log.info("Main dir "+main.logdir)
        self.logFileName = main.logdir+"/"+self.name+".session"
        main.log.info("Session log file is "+self.logFileName)
        self.handle.config('automationoptions', loglevel='info',logto=self.logFileName)
        main.log.info("Connected successfully")
        return main.TRUE
    
    def apply(self):
        try :
            main.log.info("apply the action")
            return self.handle.apply()
        except :
            main.log.error("Apply failed because of Exception"+sys.exc_info()[0])
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    
    def create(self,objectTypeString,**arguments) :
        try :
            main.log.info("creating arguments") 
            #return { result : main.TRUE,return value : self.handle.create(objectTypeString,**arguments) }
            return self.handle.create(objectTypeString,**arguments)
            #return ReturnValue(main.TRUE,self.handle.create(objectTypeString,**arguments))
        except :
            main.log.error("Operation "+str(objectTypeString)+" failed because of exception "+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE, 'error' : sys.exc_info()[0] }

    
    def config(self,handleString,**attributes) :
        try :
            main.log.info("Configure Port locations")
            self.handle.config(handleString,**attributes)
            #return { result : main.TRUE, return value : slef.handle.config(handleString,**attributes)}
            return self.handle.config(handleString,**attributes)
            #return ReturnValue(main.TRUE,self.handle.config(handleString,**attributes))
        except :
            main.log.error("Operation "+str(handleString)+" failed because of exception "+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE, 'error' : sys.exc_info()[0] } 
    
    def get(self,handleString, attribute) :
        try :
            main.log.info("Getting attributes for "+str(handleString))
            #return { result : main.TRUE , return value : self.handle.get(handleString,attribute)}
            return self.handle.get(str(handleString), attribute)
            #return ReturnValue(main.TRUE,self.handle.get(handleString, attribute))
        except :
            main.log.error("operation"+str(handleString)+"failed because of exception"+str(sys.exc_info()[0]))
            return { 'result' :main.FALSE , 'error': sys.exc_info()[0]}

    def perform(self,commandNameString, **attribute) :
        try :
            main.log.info("Performing action "+str(commandNameString))
            #return { result : main.TRUE , return value : self.handle.perform(commandNameString,**attribute)}
            return self.handle.perform(str(commandNameString), **attribute)
            #return ReturnValue(main.TRUE , self.handle.perform(commandNameString,**attribute))
        except :
            main.log.error("Operation "+str(commandNameString)+" failed because of exception "+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE, 'error' : sys.exc_info()[0] }
    
    def subscribe(self,**inputParams) :
        try :
            main.log.info("subscribe the result")
            #return { result : main.TRUE , return value : self.handle.subscribe(**inputParams)}
            return self.handle.subscribe(**inputParams)
            #return ReturnValue(main.TRUE,self.handle.subscribe(**inputParams))
        except :
            main.log.error("Operation failed because of exception "+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0] }

    def disconnect(self,hostNameString) :
        try :
            main.log.info("disconnect")
            #return { result : main.TRUE ,return value : self.handle.disconnect(hostNameString)}
            return self.handle.disconnect(str(hostNameString))
            #return ReturnValue(main.TRUE,self.handle.disconnect(hostNameString))
        except :
            main.log.error("Operation failed because of exception "+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE, 'error' : sys.exc_info()[0] }

    def sleep(self,numberSecondsInteger) :
        try :
            main.log.info("sleep time is")
            #return { result : main.TRUE , return value : self.handle.sleep(numberSecondsInteger)}
            return self.handle.sleep(str(numberSecondsInteger))
            #return ReturnValue(main.TRUE,self.handle.sleep(numberSecondsInteger))
        except :
            main.log.error("Operation failed because of exception "+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE, 'error' : sys.exc_info()[0] }

    def unsubscribe(self,resultDataSetHandleString) :
        try :
            main.log.info("unsubscribe the ports"+str(resultDataSetHandleString))
            return self.handle.unsubscribe(str(resultDataSetHandleString))
            #return { result : main.TRUE , return value : self.handle.unsubscribe(resultDataSetHandleString)}
            #return ReturnValue(main.TRUE,self.handle.unsubscribe(resultDataSetHandleString))
        except :
            main.log.error("unsubscribe"+str(resultDataSetHandleString)+" failed because of exception "+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE, 'error' : sys.exc_info()[0] }

    def delete(self,handleString) :
        try :
            main.log.info("Deleting ports"+str(handleString))
            return self.handle.delete(str(handleString))
            #return ReturnValue(main.TRUE,self.handle.delete(handleString))
        except :
            main.log.error("Deletion of "+str(handleString)+"failed because of exception "+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE, 'error' : sys.exc_info()[0] }
    def parseresults(self,csvFile) :
        try :
            main.log.info("parsing the CSV file to Data Structure format")
            input1 = '/home/paxterra/TestON/bin/untitled/*/*.csv'
            csvFile = open('input1',"rb")
	    reader = csv.reader(csvFile)
 
	    rownum <= 2
	    for row in reader:
	        # Save header row.
	        if rownum ==2 :
                    header = row
	        else:
	            colnum = 0
	            for col in row:
                        colnum += 1	             
                return (header[colnum], col)
                rownum += 3

            inputfile.close()
            return ReturnValue(main.TRUE,self.parseresults(csvFile))
        except :
            main.log.error("No such a file or directory")
            return { 'result' : main.FALSE, 'error' : sys.exc_info()[0] } 
