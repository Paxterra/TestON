#/usr/bin/env python
'''
Created on 07-Jan-2013
       
@author: Raghav Kashyap(raghavkashyap@paxterrasolutions.com)
'''

import xmldict
import re

class xmlparser :
    
    def __init__(self) :
        self.default = ''

    def parse(self,fileName) :
        '''
         This will parse the params or topo or cfg file and return content in the file as Dictionary
        '''
        self.fileName = fileName
        matchFileName = re.match(r'(.*)\.(params|topo|cfg)', self.fileName, re.M | re.I)
        if matchFileName:
            xml = open(fileName).read()
            try :
                parsedInfo = xmldict.xml_to_dict(xml)
                return parsedInfo
            except :
                print "There is no such file to parse " + fileName 
        else :
            print "file name is not correct"

    def parseParams(self,paramsPath):
        '''
         It will take the params file path and will return the params dictionary
        '''
        paramsPath = re.sub("\.","/",paramsPath) 
        paramsPath = re.sub("tests|examples","",paramsPath)
        params = self.parse(main.tests_path+paramsPath+".params")
        paramsAsString = str(params)
        return eval(paramsAsString)

    def parseTopology(self,topologyPath):
        '''
          It will take topology file path and will return topology dictionary
        '''
        topologyPath = re.sub("\.","/",topologyPath)
        topologyPath = re.sub("tests|examples","",topologyPath)
        topology = self.parse(main.tests_path+"/"+topologyPath+".topo")
        topoAsString = str(topology)
        return eval(topoAsString)
                                                                  