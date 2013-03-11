#!/usr/bin/env python
'''
Created on 28-Nov-2012

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)
'''  
class Topology:
    '''
    
    This example shows, how we can use the topology file:
    
    In topo file we can specify the component like below:
    [TOPOLOGY]   
    
        [[COMPONENT]]
            [[["Mininet1"]]]
           
    The usage of this component in the test script like below:
    
    main.Mininet1.checkIP(main.params['CASE1']['destination'])
    
    Here we are using the Mininet1 which of type Mininet 
    
    
    
    ofautomation>run Topology example 1
       will execute this example.
    '''
    def __init__(self):
        self.default = ""
                
    def CASE1(self,main):
        '''
        This will showcase the usage of Topology
        '''
        main.case("Usage of Topology")
        main.step("Mininet1 specified in Topology , using the Mininet1 to check host ip")
        result = main.Mininet1.checkIP(main.params['CASE1']['destination'])
        main.step("Verifying the result")
        utilities.assert_equals(expect=main.TRUE,actual=result,onpass="Host h2 IP address configured",onfail="Host h2 IP address didn't configured") 
        
        
