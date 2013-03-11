#!/usr/bin/env python
'''
Created on 22-Nov-2012 

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)      
'''

import struct, fcntl, os, sys, signal
import sys, re
sys.path.append("../")

from drivers.component import Component
class API(Component):
    '''
        This will define common functions for CLI included.
    '''
    def __init__(self):
        super(Component, self).__init__()
        
    def connect(self):
        '''
           Connection will establish to the remote host using ssh.
           It will take user_name ,ip_address and password as arguments<br>
           and will return the handle. 
        '''
        super(API, self).connect(self)
         
        return main.TRUE       