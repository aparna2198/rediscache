# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 02:00:44 2021

@author: APARNA
"""

d  ={}
d['name'] = "Aparna"
d['surname']  = "Jo"

import sys 
import os

currentdir = os.path.dirname('__file__')
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from rejson import Client, Path
import redis
import json 

rc = Client(host = 'lorri.redis.cache.windows.net',port=6379,decode_responses=True)
rj = Client(host='localhost', port=6380,db = 0)
rc.execute_command('SET',data.get('display_indent_id'),data)


redis_client = redis.Redis(host = "localhost",port = 6379,db = 0)
redis_client.set("transporter_profile_IND001776",json.dumps(response))

trans = json.loads(redis_client.get("transporter_profile_IND001776"))

with open('output.txt', 'w') as f_output:
    f_output.write(json.dumps(trans))



