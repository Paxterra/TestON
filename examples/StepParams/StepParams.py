#!/usr/bin/env python
'''
Created on 28-Nov-2012

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)
'''  
class StepParams:
    ''' 
    This example shows the usage of the STEP level parameters, in params file the
    [[CASE1]]
    [[[STEP1]]]
        'host'  = 'h2'
    
    We can get this STEP level parameter like :
    main.params['CASE1']['STEP1']['host']
    
    
    ofautomation>run StepParams example 1       
    '''
    def __init__(self):
        self.default = ""
                
    def CASE1(self,main):
        '''
        This example will showcase the usage of STEP level parameters to specify the host as h2
        '''
        main.case("Using STEP level parameters to specify the host as h2")
        main.step("Host IP Checking using checkIP")
        result = main.Mininet1.checkIP(main.params['CASE1']['STEP1']['host'])
        main.step("Verifying the result")
        utilities.assert_equals(expect=main.TRUE,actual=result,onpass="Host h2 IP address configured",onfail="Host h2 IP address didn't configured") 
        

    def CASE2(self,main):
        '''
                This example will showcase the usage of STEP level parameters to specify the host as h3
        '''
        main.case("Using STEP level parameters to specify the host as h3")
        main.step("Host IP Checking using checkIP")
        result = main.Mininet1.checkIP(main.params['CASE2']['STEP1']['host'])
        main.step("Verifying the result")
        utilities.assert_equals(expect=main.TRUE,actual=result,onpass="Host h3 IP address configured",onfail="Host h3 IP address didn't configured")             
