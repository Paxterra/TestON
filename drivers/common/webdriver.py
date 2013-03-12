#!/usr/bin/env python
'''
Created on 27-Feb-2013
    
@authors: Anil Kumar (anilkumar.s@paxterrasolutions.com),
          
'''
import pexpect
import struct, fcntl, os, sys, signal
import sys, re
sys.path.append("../")
from drivers.component import Component
from selenium import selenium
import unittest, time, re

class WebDriver(Component):
    '''
        This will define common functions for CLI included.
    '''
    def __init__(self):
        super(Component, self).__init__()

    def __getattr__(self, name):
        ''' 
         This will invoke, if the attribute wasn't found the usual ways.
          Here it will look for assert_attribute and will execute when AttributeError occurs.
          It will return the result of the assert_attribute.
        '''
        try:
            return getattr(self, name)
        except AttributeError:
            try:
                def experimentHandling(*args):
                   result = self.selenium_method(name,*args)
                   return result 
                return experimentHandling
            except TypeError,e:
                main.log.error("Arguments for experimental mode does not have key 'retruns'" + e)
                
    def selenium_method(self,name,*args):
        try :
            self.logfile_handler.write("\n\t"+name + str(args) +"\n")
            methodToCall = getattr(vars(self)['driver'], name)
            result = methodToCall(*args)
            return main.TRUE
        except :
            return main.FALSE   
               
    def connect(self,**connectargs):
        '''
           Connection will establish to the remote host using 
        '''
        for key in connectargs:
            vars(self)[key] = connectargs[key]
       
        self.name = self.options['name']
        try :
            connect_result = super(WebDriver, self).connect()
            url = main.componentDictionary[self.name]['url']
            host = main.componentDictionary[self.name]['host']
            selenium_port =  main.componentDictionary[self.name]['selenium_port']
            self.driver= selenium(host, int(selenium_port), "*chrome",url)
            self.driver.start()
            self.driver.open("/")
            self.verificationErrors = []
            main.log.info("Returning from connect "+str(main.TRUE))
            return main.TRUE
        except :
            return main.FALSE
    
    
    
    def wait(self,secs):
        main.log.info("Waiting for page to load")
        time.sleep(secs)
        return main.TRUE
    
    def disconnect(self):
        main.log.info("Disconnecting from WebDriver")
        #result = super(WebDriver, self).disconnect(self)
        main.log.info("Stopping Selenium")
        #self.driver.stop()
        #utilities.assert_equal([], self.verificationErrors)
        result = main.TRUE
        #self.execute(cmd="exit",timeout=120,prompt="(.*)")
    