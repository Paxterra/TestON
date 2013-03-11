#!/usr/bin/env python
'''
Created on 26-Oct-2012

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)

MininetCliDriver is the basic driver which will handle the Mininet functions
'''

import pexpect
import struct
import fcntl
import os
import signal
import re
import sys
import core.teston
sys.path.append("../")
from drivers.common.cli.emulatordriver import Emulator
from drivers.common.clidriver import CLI

class MininetCliDriver(Emulator):
    '''
        MininetCliDriver is the basic driver which will handle the Mininet functions
    '''
    def __init__(self):
        super(Emulator, self).__init__()
        self.handle = self
        self.wrapped = sys.modules[__name__]

    def connect(self, **connectargs):
        #,user_name, ip_address, pwd,options):
        # Here the main is the TestON instance after creating all the log handles.
        for key in connectargs:
            vars(self)[key] = connectargs[key]       
        
        self.name = self.options['name']
        copy = super(MininetCliDriver, self).secureCopy(self.user_name, self.ip_address,'/home/openflow/mininet/INSTALL', self.pwd,path+'/lib/Mininet/')
        self.handle = super(MininetCliDriver, self).connect(user_name = self.user_name, ip_address = self.ip_address,port = None, pwd = self.pwd)
        
        self.ssh_handle = self.handle
        
        # Copying the readme file to process the 
        if self.handle :
            #self.handle.logfile = sys.stdout
            main.log.info("Clearing any residual state or processes")
            result = self.execute(cmd="sudo mn -c",timeout=30,prompt="password")
            pattern = '[sudo]'
            if utilities.assert_matches(expect=pattern,actual=result,onpass="password is being asked",onfail="password is not being asked"):
                resultPass = self.execute(cmd="openflow",prompt="openflow",timeout=120)

            else :
                main.log.info("password is not being asked")
                pass

            cmdString = "sudo mn --topo "+self.options['topo']+","+self.options['topocount']+" --mac --switch "+self.options['switch']+" --controller "+self.options['controller']
            resultCommand = self.execute(cmd=cmdString,prompt='mininet',timeout=120)

            patterns = "Starting CLI:"
            if utilities.assert_matches(expect=patterns,actual=resultCommand,onpass="Network is being launched",onfail="Network launching is being failed "):
                return main.TRUE
            else:
                return main.FALSE

        else :
            main.log.error("Connection failed to the host "+self.user_name+"@"+self.ip_address) 
            main.log.error("Failed to connect to the Mininet")
            return main.FALSE
                       
    def pingall(self):
        '''
           Verifies the reachability of the hosts using pingall command.
        '''
        if self.handle :
            main.log.info("Checking reachabilty to the hosts using pingall")
            response = self.execute(cmd="pingall",prompt="mininet>",timeout=120)
            pattern = 'Results\:\s0\%\sdropped\s\(0\/\d+\slost\)\s*$'
            if utilities.assert_matches(expect=pattern,actual=response,onpass="All hosts are reaching",onfail="Unable to reach all the hosts"):
                return main.TRUE
            else:
                return main.FALSE
        else :
            main.log.error("Connection failed to the host") 
            return main.FALSE
        
    def pingHost(self,**pingParams):
        
        args = utilities.parse_args(["SRC","TARGET","CONTROLLER"],**pingParams)
        command = args["SRC"] + " ping -" + args["CONTROLLER"] + " " +args ["TARGET"]
        response = self.execute(cmd=command,prompt="mininet",timeout=120 )
        if utilities.assert_matches(expect='0% packet loss',actual=response,onpass="No Packet loss",onfail="Host is not reachable"):
            main.log.info("PING SUCCESS WITH NO PACKET LOSS")
            main.last_result = main.TRUE 
            return main.TRUE
        else :
            main.log.error("PACKET LOST, HOST IS NOT REACHABLE")
            main.last_result = main.FALSE
            return main.FALSE
        
    
    def checkIP(self,host):
        '''
            Verifies the host's ip configured or not.
        '''
        if self.handle :
            main.log.info("Pinging host "+host) 
            response = self.execute(cmd=host+" ifconfig",prompt="mininet>",timeout=120)

            pattern = "inet\s(addr|Mask):([0-1]{1}[0-9]{1,2}|2[0-4][0-9]|25[0-5]|[0-9]{1,2}).([0-1]{1}[0-9]{1,2}|2[0-4][0-9]|25[0-5]|[0-9]{1,2}).([0-1]{1}[0-9]{1,2}|2[0-4][0-9]|25[0-5]|[0-9]{1,2}).([0-1]{1}[0-9]{1,2}|2[0-4][0-9]|25[0-5]|[0-9]{1,2})"
            if utilities.assert_matches(expect=pattern,actual=response,onpass="Host Ip configured properly",onfail="Host IP didn't found") :
                return main.TRUE
            else:
                return main.FALSE
        else :
            main.log.error("Connection failed to the host") 
        
    def dump(self):
        main.log.info("Dump node info")
        self.execute(cmd = 'dump',prompt = 'mininet>',timeout = 10)
        return main.TRUE
            
    def intfs(self):
        main.log.info("List interfaces")
        self.execute(cmd = 'intfs',prompt = 'mininet>',timeout = 10)
        return main.TRUE
    
    def net(self):
        main.log.info("List network connections")
        self.execute(cmd = 'net',prompt = 'mininet>',timeout = 10)
        return main.TRUE
    
    def iperf(self):
        main.log.info("Simple iperf TCP test between two (optionally specified) hosts")
        self.execute(cmd = 'iperf',prompt = 'mininet>',timeout = 10)
        return main.TRUE
    
    def iperfudp(self):
        main.log.info("Simple iperf TCP test between two (optionally specified) hosts")
        self.execute(cmd = 'iperfudp',prompt = 'mininet>',timeout = 10)
        return main.TRUE
    
    def nodes(self):
        main.log.info("List all nodes.")
        self.execute(cmd = 'nodes',prompt = 'mininet>',timeout = 10)    
        return main.TRUE
    
    def pingpair(self):
        main.log.infoe("Ping between first two hosts")
        self.execute(cmd = 'pingpair',prompt = 'mininet>',timeout = 20)
        
        if utilities.assert_matches(expect='0% packet loss',actual=response,onpass="No Packet loss",onfail="Hosts not reachable"):
            main.log.info("Ping between two hosts SUCCESS")
            main.last_result = main.TRUE 
            return main.TRUE
        else :
            main.log.error("PACKET LOST, HOSTS NOT REACHABLE")
            main.last_result = main.FALSE
            return main.FALSE
    
    def link(self,**linkargs):
        '''
        Bring link(s) between two nodes up or down
        '''
        main.log.info('Bring link(s) between two nodes up or down')
        args = utilities.parse_args(["END1","END2","OPTION"],**linkargs)
        end1 = args["END1"] if args["END1"] != None else ""
        end2 = args["END2"] if args["END2"] != None else ""
        option = args["OPTION"] if args["OPTION"] != None else ""
        command = "link "+str(end1) + " " + str(end2)+ " " + str(option)
        response = self.execute(cmd=command,prompt="mininet>",timeout=10)
        return main.TRUE
        

    def dpctl(self,**dpctlargs):
        '''
         Run dpctl command on all switches.
        '''
        main.log.info('Run dpctl command on all switches')
        args = utilities.parse_args(["CMD","ARGS"],**dpctlargs)
        cmd = args["CMD"] if args["CMD"] != None else ""
        cmdargs = args["ARGS"] if args["ARGS"] != None else ""
        command = "dpctl "+cmd + " " + str(cmdargs)
        response = self.execute(cmd=command,prompt="mininet>",timeout=10)
        return main.TRUE
   
        
    def get_version(self):
        file_input = path+'/lib/Mininet/INSTALL'
        version = super(Mininet, self).get_version()
        pattern = 'Mininet\s\w\.\w\.\w\w*'
        for line in open(file_input,'r').readlines():
            result = re.match(pattern, line)
            if result:
                version = result.group(0)
                
            
        return version    

    def disconnect(self,handle):
        
        response = ''
        if self.handle:
            self.handle = handle
            response = self.execute(cmd="exit",prompt="(.*)",timeout=120)
        else :
            main.log.error("Connection failed to the host")
            response = main.FALSE
        return response  

if __name__ != "__main__":
    import sys
    sys.modules[__name__] = MininetCliDriver()
