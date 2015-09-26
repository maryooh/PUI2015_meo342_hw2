import json
import urllib2

API_KEY = '9c0690a6-de1f-48a4-ab8c-8db536692b7d'
BUS_LINE = 'B52'

url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + API_KEY +'&VehicleMonitoringDetailLevel=calls&LineRef=' + BUS_LINE
request = urllib2.urlopen(url)
data = json.loads(request.read())
print data