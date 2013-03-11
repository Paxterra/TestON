#!/usr/bin/env python
'''
Created on 26-Oct-2012 

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)      
''' 
import pexpect
import struct, fcntl, os, sys, signal
import sys
sys.path.append("../")
from drivers.common.clidriver import CLI

class Emulator(CLI):
    # The common functions for emulator included in emulatordriver
    def __init__(self):
        super(CLI, self).__init__()
        