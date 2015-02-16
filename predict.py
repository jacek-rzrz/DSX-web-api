# sample code for making predictions
# using the DSX web API

import sys, json, urllib2

# setup:
endpoint = ''

apiKey   = ''

data = json.dumps(
  { 'data' :
    [
      {
      },  
      {
      },
    ] 
  }
)

url = endpoint + '?k=' + apiKey

# (HTTP POST)
request = urllib2.Request(url, data, {'Content-Type':'application/json'})

# call API:
print 'Making a {0} request...'.format(request.get_method())
try:
  responseStr  = urllib2.urlopen(request).read()
except urllib2.HTTPError as e:
  print e
  sys.exit(1)

# parse response:
responseJson = json.loads(responseStr)

# pretty print:
print json.dumps(responseJson, indent=3)
