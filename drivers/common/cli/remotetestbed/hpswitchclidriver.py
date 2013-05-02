#!/usr/bin/env python
'''
Created on 12-Feb-2013

@author: Anil Kumar (anilkumar.s@paxterrasolutions.com)


    TestON is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    TestON is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.



HPSwitchCliDriver is the basic driver which will handle the Mininet functions
'''

import pexpect
import struct
import fcntl
import os
import signal
import re
import sys
import time

sys.path.append("../")

#from drivers.common.cli.remotetestbeddriver import RemoteTestBedDriver
from drivers.component import Component
class HPSwitchCliDriver(Component):
    '''
        HPSwitchCliDriver is the basic driver which will handle the Mininet functions
    '''
    def __init__(self):
        super(Component, self).__init__()
        
    def connect(self,**connectargs):
        
        for key in connectargs:
            vars(self)[key] = connectargs[key]
        
        self.name = self.options['name']

        self.handle = super(HPSwitchCliDriver,self).connect()
        #if self.handle :
        #    main.log.info("Connected "+self.name)
            #self.execute(cmd="\r",prompt="\$",timeout=10)
            #self.execute(cmd="pmshell",prompt="\>",timeout=10)
            # self.execute(cmd="2\r",prompt="\#|\>|$",timeout=10)
            
        #    return self.handle
        #else :
        #   main.FALSE
        return main.TRUE
    
    def configure(self,commandlist):
        for command in commandlist:
            self.execute(cmd=command,prompt="\#|\>",timeout=10)
    
    def show(self, *options, **def_args ):
        '''Possible Options :['access-list', 'accounting', 'alias', 'arp', 'arp-protect', 'authentication', 'authorization', 'autorun', 'bandwidth', 'banner', 'boot-history', 'cdp', 'class', 'config', 'console', 'cpu', 'crypto', 'debug', 'dhcp-relay', 'dhcp-snooping', 'dhcpv', 'diagnostic-level', 'distributed-trunking', 'encrypt-credentials', 'energy-efficient-e...', 'fastboot', 'fault-finder', 'feature-coordinator', 'filter', 'flash', 'front-panel-security', 'gvrp', 'history', 'igmp', 'igmp-proxy', 'include-credentials', 'interfaces', 'ip', 'ip-recv-mac-address', 'ipv', 'jumbos', 'key-chain', 'lacp', 'licenses', 'link-keepalive', 'lldp', 'lockout-mac', 'logging', 'loop-protect', 'mac-address', 'mac-count-notify', 'mac-notify', 'management', 'mesh', 'modules', 'monitor', 'name', 'openflow', 'policy', 'port-access', 'port-security', 'power-over-ethernet', 'qinq', 'qos', 'radius', 'rate-limit', 'reload', 'rmon', 'route-map', 'running-config', 'savepower', 'secure-mode', 'server-group', 'services', 'session-list', 'sflow', 'snmp-server', 'snmpv', 'sntp', 'spanning-tree', 'static-mac', 'statistics', 'switch-interconnect', 'syslog', 'system', 'tacacs', 'tech', 'telnet', 'terminal', 'timep', 'trunks', 'uplink-failure-det...', 'uptime', 'usb-port', 'version', 'vlans', 'vrrp', 'wireless-services']'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_arp(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show arp "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_cdp(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show cdp "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_class(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show class "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_alias(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show alias "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_banner(self, *options, **def_args ):
        '''Possible Options :['vlan']'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show banner "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_config(self, *options, **def_args ):
        '''Possible Options :['group']'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show config "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_autorun(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show autorun "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_bandwidth(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show bandwidth "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_accounting(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show accounting "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_accesslist(self, *options, **def_args ):
        '''Possible Options :['config', 'ports', 'radius', 'resources', 'tunnel', 'vlan']'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show access-list "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_banner_vlan(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show banner vlan "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_arpprotect(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show arp-protect "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_config_group(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show config group "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_boothistory(self, *options, **def_args ):
        '''Possible Options :['statistics']'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show boot-history "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_authorization(self, *options, **def_args ):
        '''Possible Options :['sessions']'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show authorization "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_authentication(self, *options, **def_args ):
        '''Possible Options :['all']'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show authentication "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_accesslist_vlan(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show access-list vlan "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_accesslist_ports(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show access-list ports "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_authentication_all(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show authentication all "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_accesslist_config(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show access-list config "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_accesslist_radius(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show access-list radius "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_accesslist_tunnel(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show access-list tunnel "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_accesslist_resources(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show access-list resources "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_authorization_sessions(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show authorization sessions "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE

    def show_boothistory_statistics(self, *options, **def_args ):
        '''Possible Options :[]'''
        arguments= ''
        for option in options:
            arguments = arguments + option +' ' 
        prompt = def_args.setdefault('prompt',self.prompt)
        timeout = def_args.setdefault('timeout',self.timeout)
        self.execute( cmd= "show boot-history statistics "+ arguments, prompt = prompt, timeout = timeout ) 
        return main.TRUE
