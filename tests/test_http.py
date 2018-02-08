

import urllib2
import urllib
import json
# Get a scitoken from the demo.scitokens.org service

demo_json = { 
"payload": {
'aud': 'test',
'scp': 'read:/protected',
'aud': 'flask'
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

# Make a connection to the local flask instance
req = urllib2.Request("http://localhost:1234/auth")

req.add_header('X-Original-Method', 'GET')
req.add_header('X-Original-URI', '/protected/stuff')
req.add_header('Authorization', 'Bearer {0}'.format(the_page))
resp = urllib2.urlopen(req)

content = resp.read()