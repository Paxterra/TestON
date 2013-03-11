#!/usr/bin/env python
'''
Created on 29-Oct-2012

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)
''' 
class MininetTest:
    '''
    Testing of the some basic Mininet functions included here
    '''
    
    def __init__(self):
        self.default = ""
                
    def CASE1(self,main):
        '''
        Testing the configuration of the host by using checkIP functionof Mininet driver
        '''
        main.case("Testing the configuration of the host")
        main.step("Host IP Checking using checkIP")
        result = main.Mininet1.checkIP(main.params['CASE1']['destination'])
        main.step("Verifying the result")
        utilities.assert_equals(expect=main.TRUE,actual=result,onpass="Host h2 IP address configured",onfail="Host h2 IP address didn't configured") 
 
    def CASE2(self,main):
        '''
        Testing of the reachability of the hosts by using pingall of Mininet driver
        '''
        main.case("Testing Reachabilty of all the hosts")
        main.step("Checking Hosts reachability by using pingall")
        result = main.Mininet1.pingall()
        main.step("Verifying the result")
        utilities.assert_equals(expect=main.TRUE,actual=result,onpass="All hosts are reacchable",onfail="Hosts are not reachable")
           
            
