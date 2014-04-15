#!/usr/bin/python/
'''
Created on 21-FEB-2014
       
    TestON is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    TestON is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with TestON.  If not, see <http://www.gnu.org/licenses/>.		


'''
import pexpect
import struct
import fcntl
import os
import signal
import re
import sys
import requests
import json
import httplib
import httplib2
import urllib
from requests.auth import HTTPBasicAuth
import core.teston
sys.path.append("../")
from drivers.common.restapidriver import RESTAPI
class OdlDriver(RESTAPI):
    baseUrl = 'http://localhost:8080/controller/nb/v2/'
    headers={"accept":"application/json","content-type":"application/json"}
   
    '''
        OdlCliDriver is the controller driver which will handle the Mininet functions
    '''
    def __init__(self):
        super(RESTAPI, self).__init__()
        self.handle = self
        self.wrapped = sys.modules[__name__]
        self.flag = 0
    def connect(self, **connectargs):
        #,user_name, ip_address, pwd,options):
        # Here the main is the TestON instance after creating all the log handles.
        for key in connectargs:
            vars(self)[key] = connectargs[key] 
        self.name = self.options['name']
        self.handle = super(OdlDriver, self).connect(user_name = self.user_name, ip_address = self.ip_address,port = None, pwd = self.pwd)
        self.ssh_handle = self.handle
        if self.handle :
            self.handle.logfile = sys.stdout
            '''main.log.info("killall existing controllers")
            self.execute(cmd="sudo killall controllers",prompt="password",timeout=15)
            self.execute(cmd="opendaylight",prompt="$",timeout=10)
            main.log.info("Enter inside the opendaylight folder")
            self.execute(cmd="cd opendaylight",timeout=30,prompt="$")
            main.log.info("Executing the opendaylight controller")
            pattern ='\sController\sis\snow\slistening\son\sany\:6633'
            result = self.execute(cmd="./run.sh",prompt=pattern,timeout=250)'''
            return main.TRUE
        else :
            main.log.info("opendaylight execution is failed")
            return main.FALSE

    def get_topology(self,**args) :
        try :
            arg = utilities.parse_args(["CONTAINER"],**args)            
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl + 'topology/' + arg["CONTAINER"], "GET")
            edgeProperties = json.loads(content)
            odlEdges = edgeProperties['edgeProperties']
            main.log.info(odlEdges)
            return resp['status']
                  
        except :
            main.log.error("getting topology failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    
    def list_subnet(self,**args):
        try :
            arg = utilities.parse_args(["CONTAINER"],**args)            
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl + 'subnetservice/' + arg["CONTAINER"]+ '/subnets/', "GET")
            subnets = json.loads(content)
            main.log.info(subnets)
            return resp['status']
        except :
            main.log.error("getting subnets failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    def list_hosts(self,**args) :
        try :
            arg = utilities.parse_args(["CONTAINER"],**args)                        
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl + 'hosttracker/' + arg["CONTAINER"]+ '/hosts/active/', "GET")
            hosts = json.loads(content)
            main.log.info(hosts)
            return resp['status']
        except :
            main.log.error("getting hosts failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]} 

    def list_containers(self,**args) :
        try :
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl + 'containermanager/containers/', "GET")
            l_containers = json.loads(content)
            main.log.info(l_containers)
            return resp['status']
        except :
            main.log.error("getting containers failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    
    def list_connections(self,**args):
        try :
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl + 'connectionmanager/nodes/', "GET")
            connections = json.loads(content)
            main.log.info(connections)
            return resp['status']
        except :
            main.log.error("getting connections failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def list_nodes(self,**args) :
        try :
            arg = utilities.parse_args(["CONTAINER"],**args)
            
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl + 'switchmanager/' + arg["CONTAINER"]+'/nodes/', "GET")
            nodes = json.loads(content)
            main.log.info(nodes)
            return resp['status']
        except :
            main.log.error("getting nodes failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def list_switchproperties(self,**args) :
        try :
            main.log.info("list all connectors and properties for switches ")
            arg = utilities.parse_args(["CONTAINER","DPID"],**args)            
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl + 'switchmanager/' + arg["CONTAINER"]+ '/node/OF/'+arg["DPID"], "GET")
            switch_properties = json.loads(content)
            main.log.info(switch_properties)
            return resp['status']
        except :
            main.log.error("getting list switch properties failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def flow_stats(self,**args) :
        try :
            main.log.info("default flow statistics")
            arg = utilities.parse_args(["CONTAINER"],**args)            
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl + 'statistics/' + arg["CONTAINER"]+ '/flow/', "GET")
            flows = json.loads(content)
            main.log.info(flows)
            return resp['status']
        except :
            main.log.error("getting flows failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def port_stats(self,**args) :
        try :
            main.log.info("default port statistics")
            arg = utilities.parse_args(["CONTAINER"],**args)            
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl + 'statistics/' + arg["CONTAINER"]+ '/port/', "GET")
            ports = json.loads(content)
            main.log.info(ports)
            return resp['status']
        except :
            main.log.error("getting ports failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    def table_stats(self,**args) :
        try :
            main.log.info("default table statistics")
            arg = utilities.parse_args(["CONTAINER"],**args)            
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl + 'statistics/' + arg["CONTAINER"]+ '/table/', "GET")
            table = json.loads(content)
            main.log.info(table)
            return resp['status']
        except :
            main.log.error("getting tables failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def add_userlink(self,**args) :
        try :
            arg = utilities.parse_args(["CONTAINER","LINK","INPUT"],**args)
            main.log.info("adding links to topology")
            link_input= arg["INPUT"]
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl+'topology/'+arg["CONTAINER"]+'/userLink/'+arg["LINK"],"PUT",body=json.dumps(link_input),headers=self.headers)
            return resp['status']
        except :
            main.log.error("inserting links failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def remove_userlink(self,**args):
        try :
            arg = utilities.parse_args(["CONTAINER","LINK","INPUT"],**args)
            main.log.info("removing link from topology")
            h = httplib2.Http(".cache")
            h.add_credentials('admin', 'admin')
            resp, content = h.request(self.baseUrl+'topology/'+arg["CONTAINER"]+'/userLink/'+arg["LINK"],"DELETE",headers=self.headers)
            return resp['status']
        except :
            main.log.error("inserting links failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]} 

    def create_container(self,**args) :
        try :            
            arg = utilities.parse_args(["CONTAINER","INPUT"],**args)
            
            main.log.info("creating container to the switches")
            container_body = arg["INPUT"]
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'containermanager/container/'+arg["CONTAINER"],"PUT",body=json.dumps(container_body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("create container failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    
    def remove_container(self,**args) :
        try :            
            arg = utilities.parse_args(["CONTAINER"],**args)
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'containermanager/container/'+arg["CONTAINER"],"DELETE",headers=self.headers)
            return resp['status']
        except:
            main.log.error("create container failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def add_flowspecs(self,**args):
        try :            
            arg = utilities.parse_args(["CONTAINER","INPUT","NAME"],**args)
            main.log.info("adding flow specs to the hosts")
            flowspec_body = arg["INPUT"]
            #{"name" : "h1toh3","nwSrc" : "10.0.0.1","nwDst" : "10.0.0.3"}
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'containermanager/container/'+arg["CONTAINER"]+'/flowspec/'+arg["NAME"],"PUT",body=json.dumps(flowspec_body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("adding flowspec failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def add_flow(self,**args):
        try :
            main.log.info("adding flow to the switches")
            arg = utilities.parse_args(["CONTAINER","DPID","INPUT","NAME"],**args)         
            main.log.info("adding flow to the Switches")
            flow_body = arg["INPUT"]
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'flowprogrammer/'+arg["CONTAINER"]+'/node/OF/'+arg["DPID"]+'/staticFlow/'+arg["NAME"],"PUT",body=json.dumps(flow_body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("adding flows failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    
    def delete_flow(self,**args) :
        try :
            main.log.info("deleting the flows")
            arg = utilities.parse_args(["CONTAINER","DPID","NAME"],**args)            
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp,content = h.request(self.baseUrl+'flowprogrammer/'+arg["CONTAINER"]+'/node/OF/'+arg["DPID"]+'/staticFlow/'+arg["NAME"],"DELETE",headers=self.headers)
            return resp['status']
        except:
            main.log.error("deleting flow failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    def add_host(self,**args):
        try :
            arg = utilities.parse_args(["CONTAINER","INPUT","IPADDRESS"],**args)
            host_body = arg["INPUT"]
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'hosttracker/'+arg["CONTAINER"]+'/address/'+arg["IPADDRESS"],"PUT",body=json.dumps(host_body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("adding host failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
    def remove_host(self,**args):
        try :
            arg = utilities.parse_args(["CONTAINER","IPADDRESS"],**args)
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'hosttracker/'+arg["CONTAINER"]+'/address/'+arg["IPADDRESS"],"DELETE",headers=self.headers)
            return resp['status']
        except:
            main.log.error("removing host failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def add_subnet(self,**args):
        try :
            arg = utilities.parse_args(["CONTAINER","NAME","INPUT"],**args)
            subnet_body=arg["INPUT"]
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'subnetservice/'+arg["CONTAINER"]+'/subnet/'+arg["NAME"],"PUT",body=json.dumps(subnet_body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("adding subnet failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]} 

    def remove_subnet(self,**args):
        try :
            arg = utilities.parse_args(["CONTAINER","NAME"],**args)
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'subnetservice/'+arg["CONTAINER"]+'/subnet/'+arg["NAME"],"DELETE",headers=self.headers)
            return resp['status']
        except:
            main.log.error("removing subnet failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]} 

    def add_static_route(self,**args):
        try :
            arg = utilities.parse_args(["CONTAINER","INPUT","NAME"],**args)
            route_body = arg["INPUT"]
	    #{"name":"route1","prefix":"192.168.1.0/24","nextHop":"10.0.0.2"}
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'staticroute/'+arg["CONTAINER"]+'/route/'+arg["NAME"],"PUT",body=json.dumps(route_body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("adding static route failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def remove_static_route(self,**args):
        try :
            arg = utilities.parse_args(["CONTAINER","NAME"],**args)
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'staticroute/'+arg["CONTAINER"]+'/route/'+arg["NAME"],"DELETE",headers=self.headers)
            return resp['status']
        except:
            main.log.error("removing static route failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def add_node_connectors(self,**args):
        try :
            arg = utilities.parse_args(["CONTAINER","INPUT"],**args)		
            node_connector=arg["INPUT"]
	    h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'containermanager/container/'+arg["CONTAINER"]+'/nodeconnector',"PUT",body=json.dumps(node_connector),headers=self.headers)
            return resp['status']
        except:
            main.log.error("adding node connector failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def remove_node_connector(self,**args):
        try :
            arg = utilities.parse_args(["CONTAINER","INPUT"],**args)		
            nodeconeector_body=arg["INPUT"]
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'containermanager/container/'+arg["CONTAINER"]+'/nodeconnector',"DELETE",body=json.dumps(node_connector),headers=self.headers)
            return resp['status']
        except:
            main.log.error("remove node connector failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def remove_flowspec(self,**args):
        try :
            arg = utilities.parse_args(["CONTAINER","NAME"],**args)		
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'containermanager/container/'+arg["CONTAINER"]+'/flowspec/'+arg["NAME"],"DELETE",headers=self.headers)
            return resp['status']
        except:
            main.log.error("removing flowspec failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def connect_to_mininet(self,**args):
        try : 
            arg = utilities.parse_args(["PORT","IPADDRESS"],**args)		
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'connectionmanager/node/MININET/address/'+arg["IPADDRESS"]+'/port/'+arg["PORT"],"PUT",headers=self.headers)
            return resp['status']
        except:
            main.log.error("connecting mininet failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def create_bridge(self,**args):
        try :
            arg = utilities.parse_args(["NAME"],**args)		
            bridge_body={}
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'networkconfig/bridgedomain/bridge/OVS/MININET/'+arg["NAME"],"POST",body=json.dumps(bridge_body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("creating bridge failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def remove_port_on_ethernet(self,**args):
        try :
            arg = utilities.parse_args(["ETHERNET","SWITCHNAME"],**args)		
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'networkconfig/bridgedomain/port/OVS/MININET/'+arg["SWITCHNAME"]+'/'+arg["ETHERNET"],"DELETE",headers=self.headers)
            return resp['status']
        except:
            main.log.error("removing port failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def create_port_on_ethernet(self,**args):
        try :
	    arg = utilities.parse_args(["ETHERNET","SWITCHNAME","INPUT"],**args)
            port_body = arg["INPUT"]
	    #{"type":"patch", "CUSTOM":{"peer":"s2-eth3"}}
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'networkconfig/bridgedomain/port/OVS/MININET/'+arg["SWITCHNAME"]+'/'+arg["ETHERNET"],"PUT",body=json.dumps(port_body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("creating port failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def add_bandwidth(self,**args):
        try :
	    arg = utilities.parse_args(["CONTAINER","DPID","BANDWIDTH"],**args)
            body={}
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'switchmanager/'+arg["CONTAINER"]+'/nodeconnector/OF/'+arg["DPID"]+'/OF/2/property/bandwidth/'+arg["BANDWIDTH"],"PUT",body=json.dumps(body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("adding bandwidth failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]} 

    def remove_bandwidth(self,**args):
        try :
	    arg = utilities.parse_args(["CONTAINER","DPID"],**args)
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'switchmanager/'+arg["CONTAINER"]+'/nodeconnector/OF/'+arg["DPID"]+'/OF/2/property/bandwidth/',"DELETE",headers=self.headers)
            return resp['status']
        except:
            main.log.error("removing bandwidth failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]} 

    def add_property_description(self,**args):
        try :
	    arg = utilities.parse_args(["CONTAINER","DPID"],**args)
            body={}
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'switchmanager/'+arg["CONTAINER"]+'/node/OF/'+arg["DPID"]+'/property/description/Switch2',"PUT",body=json.dumps(body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("adding property description failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def remove_property_description(self,**args):
        try :
	    arg = utilities.parse_args(["CONTAINER","DPID"],**args)
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'switchmanager/'+arg["CONTAINER"]+'/node/OF/'+arg["DPID"]+'/property/description',"DELETE",headers=self.headers)
            return resp['status']
        except:
            main.log.error("Removing property description failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]} 

    def save_config(self,**args):
        try :
	    arg = utilities.parse_args(["CONTAINER"],**args)
            body={}
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'switchmanager/'+arg["CONTAINER"]+'/save',"POST",body=json.dumps(body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("Save configuration failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def list_restart_flow(self,**args):
        try :
	    arg = utilities.parse_args(["CONTAINER"],**args)
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'flowprogrammer/'+arg["CONTAINER"],"GET",headers=self.headers)
            return resp['status']
        except:
            main.log.error("Restarting flows failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def list_flowspecs(self,**args):
        try :
	    arg = utilities.parse_args(["CONTAINER"],**args)
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'containermanager/container/'+arg["CONTAINER"]+'/flowspecs',"GET",headers=self.headers)
            return resp['status']
        except:
            main.log.error("list flowspecs failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def disconnect_mininet(self,**args):
        try :
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'connectionmanager/node/OVS/MININET',"DELETE",headers=self.headers)
            return resp['status']
        except:
            main.log.error("disconnecting mininet failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}          
    def create_port(self,**args):
        try :
	    arg = utilities.parse_args(["NAME"],**args)
            body = {}
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'networkconfig/bridgedomain/port/OVS/MININET/'+arg["NAME"],"POST",body=json.dumps(body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("disconnecting mininet failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}

    def add_user(self,**args):
        try :
            arg = utilities.parse_args(["INPUT"],**args)
            body=arg["INPUT"]
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'usermanager/users',"POST",body=json.dumps(body),headers=self.headers)
            return resp['status']
        except:
            main.log.error("adding property description failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]} 

    def remove_user(self,**args) :
        try :
            arg = utilities.parse_args(["NAME"],**args)
            h = httplib2.Http(".cache")
            h.add_credentials('admin','admin')
            resp, content = h.request(self.baseUrl+'usermanager/users/'+arg["NAME"],"DELETE",headers=self.headers)
            return resp['status']
        except:
            main.log.error("adding property description failed because of"+str(sys.exc_info()[0]))
            return { 'result' : main.FALSE , 'error' : sys.exc_info()[0]}
             
if __name__ != "__main__":
    import sys
    sys.modules[__name__] = OdlDriver()
