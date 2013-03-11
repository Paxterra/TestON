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
    
    def search_bus(self):
        try :
            self.driver.click("id=search_submit_btn")
            self.driver.wait_for_page_to_load("300000")
            self.wait(10)
            return main.TRUE
        except :
            return main.FALSE
        
    def select_bus(self):
        try :
            self.driver.click("//html/body/div[2]/div/div[2]/div/table/tbody/tr/td[2]/div/div/div/table/tbody/tr/td[6]/a/img")
            self.wait(7)
            self.wait_for_element("id=span_2_12")
            self.wait(7)
            return main.TRUE
        except :
            try :
                self.driver.click("//html/body/div[2]/div/div[2]/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[2]/div[2]/div/table/tbody/tr/td[4]/a/span")
                self.wait(7)
                self.driver.click("//html/body/div[2]/div/div[2]/div/table/tbody/tr/td[2]/div/div/div/table/tbody/tr/td[6]/a/img")
                self.wait(7)
                self.wait_for_element("id=span_2_12")
                self.wait(7)
                return main.TRUE
            except :
                return main.FALSE
            
    def select_seat(self):
        try :
            self.driver.click("id=span_2_12")
            return main.TRUE
        except :
            return main.FALSE
        
    def fill_details(self,**details):
        args = utilities.parse_args(["TITLE","PASSENGER_NAME","PASSENGER_AGE","DROP_OFF","EMAIL","PHONE_NUMBER","ID_CARD_NUMBER","ID_CARD_ISSUED","ADDRESS"],**details)
        try :
            self.driver.select("id=ticket_title_C3", "label="+args["TITLE"])
            self.driver.type("id=ticket_passenger_name_C3", args["PASSENGER_NAME"])
            self.driver.type("id=ticket_passenger_age_C3", args["PASSENGER_AGE"])
            self.driver.select("id=searchbus_drop_off", "label="+args["DROP_OFF"])
            self.driver.type("id=ticket_email", args["EMAIL"])
            self.driver.type("id=ticket_phone_number", args['PHONE_NUMBER'])
            self.driver.type("id=id_card_number", args['ID_CARD_NUMBER'])
            self.driver.type("id=id_card_issued_details",args['ID_CARD_ISSUED'] )
            self.driver.type("id=ticket_address", args['ADDRESS'])
            self.driver.click("id=terms_conditions")
            return main.TRUE
        except :
            return main.FALSE
        
    def deselect_seat(self):
        try :
            self.wait(10)
            self.driver.click("id=span_2_12")
            self.driver.stop()
            return main.TRUE
        except :
            return main.FALSE
        
    def wait_for_element(self,element):
        main.log.info("Waiting for element "+ element)
        try :
            for i in range(60):
                try:
                    if self.driver.is_element_present(element): 
                       break
                except: 
                    pass
                time.sleep(1)    
            else:
                main.log.error("Time out : "+element +"Not present")
                return main.FALSE
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
    