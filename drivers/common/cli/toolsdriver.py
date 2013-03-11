#!/usr/bin/env python
'''
Created on 26-Nov-2012

@author: Raghav Kashyap(raghavkashyap@paxterrasolutions.com)
'''  
import pexpect
import struct, fcntl, os, sys, signal
import sys
sys.path.append("../")
from drivers.common.clidriver import CLI


class Tools(CLI):
    # The common functions for Tools included in toolsdriver
    def __init__(self):
        super(CLI, self).__init__()
