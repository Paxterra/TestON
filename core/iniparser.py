#/usr/bin/env python
'''
Created on 07-Jan-2013
       
@author: Raghav Kashyap(raghavkashyap@paxterrasolutions.com)
'''

import re
from configobj import ConfigObj
class iniparser:
    '''
    Manages authoring, parsing and execution of the test. Sub components are
    Test-Topology parser
    Module that parses the test from plain English and topology
    from a specification file and prepares for execution.
    Test sequencer 
    Module that executes the tests case by case,
    step by step adding ability for step by step pause and debug later.
    Object loader
    Module that connects and loads all the component connection objects 
    for access in the test 
    '''
    def __init__(self) :
        self.default = ''

    def parse(self,fileName):
        '''
         This will parse the params or topo or cfg file and return content in the file as Dictionary
        '''
        self.fileName = fileName
        matchFileName = re.match(r'(.*)\.(params|topo)',self.fileName,re.M|re.I)
        if matchFileName:
            try :
                parsedInfo = ConfigObj(self.fileName)
                return parsedInfo
            except :
                print "There is no such file to parse "+fileName
        else:
            return 0

    def parseParams(self,paramsPath):
        '''
        It will take the params file path and will return the params dictionary
        '''

        paramsPath = re.sub("\.","/",paramsPath)
        paramsPath = re.sub("tests|examples","",paramsPath)
        #print main.tests_path+"/"+paramsPath+".params"
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

