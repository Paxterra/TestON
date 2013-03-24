#/usr/bin/env python
'''
Created on 07-Jan-2013
       
@author: Raghav Kashyap(raghavkashyap@paxterrasolutions.com)
'''

import re
import json
class JsonParser:
    '''
    Module that parses the response Json to Dictionary and Vice versa. 
    '''
    def __init__(self) :
        self.default = ''

    def response_parse(self,json_response):
        '''
         This will parse the json formatted string and return content as Dictionary
        '''
        response_dict = {}
        try :
            response_dict = json.loads(json_response)
        except :
            main.log.error("Json Parser is unable to parse the string")
        return response_dict         
    
    '''
    
    def dict_json(self,response_dict):
        
        # This will parse the Python Dictionary and return content as Json string.
        
        json_response = {}
        try :
            json_response = json.dumps(response_dict)
        except :
            main.log.error("Json Parser is unable to parse the string")
        return json_response  
    '''