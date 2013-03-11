#!/usr/bin/env python
'''
Created on 29-Nov-2012 

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)      
'''  
import sys
sys.path.append("../")
from drivers.common.apidriver import API

class Controller(API):
    # The common functions for emulator included in emulatordriver
    def __init__(self):
        super(API, self).__init__()
        