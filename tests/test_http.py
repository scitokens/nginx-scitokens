#!/usr/bin/python

import urllib2
import urllib
import json
import requests
import random
import tempfile
import os
# Get a scitoken from the demo.scitokens.org service

hostname = "hostname"
request_path = "/protected/stuff/blah"
scope = "write:/stuff"

demo_json = { 
    "payload": {
        'scp': scope,
        'aud': 'testing'
    },
    "header": {
        'alg': 'RS256',
        'typ': 'JWT'
    }
}

data = json.dumps({
        'payload': json.dumps(demo_json['payload']),
        'header': json.dumps(demo_json['header'])
        })

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36','Content-Type': 'application/json'}
req = urllib2.Request("https://demo.scitokens.org/issue", data, headers=head)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page

url = "https://{0}:443{1}".format(hostname, request_path)

# Make a connection to the local flask instance
req = urllib2.Request(url, "this is the data")
req.get_method = lambda: 'PUT'

#req.add_header('X-Original-Method', 'PUT')
#req.add_header('X-Original-URI', '/protected/stuff/is/cool')
req.add_header('Authorization', 'Bearer {0}'.format(the_page))
resp = urllib2.urlopen(req)

content = resp.read()

print "Creating a random large file to upload"
headers = { 'Authorization': 'Bearer {0}'.format(the_page)}

fout = tempfile.NamedTemporaryFile(delete=False)
fout.write(os.urandom(1024 * 1024 * 50))
fout.close()
files = { 'file': open(fout.name) }
url = url + "_big"
requests.put(url, files=files, headers=headers)

os.unlink(fout.name)