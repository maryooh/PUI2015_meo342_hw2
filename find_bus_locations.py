import json
import urllib2
import sys

#load json file from MTA Bus Times website using the provided developer key
#url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + API_KEY +'&VehicleMonitoringDetailLevel=calls&LineRef=' + BUS_LINE
#request = urllib2.urlopen(url)
#data = json.loads(request.read())

def findbusloc(API_KEY, BUS_LINE):
	API_KEY = '9c0690a6-de1f-48a4-ab8c-8db536692b7d'
	#I had the below as BUS_LINE = 'B52', but realized this would set it at one busline
	BUS_LINE = sys.argv[2]
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (API_KEY, BUS_LINE)
	#jsonFile = open(url, 'r')
	data = json.load(open(url,'r'))
	vehicles = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

	for b in vehicles:
		if b['PublishedLineName'] == BUS_LINE:
			busno = b['vehicleref'][10:]
			busLat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
			busLon = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

			print 'Bus Line :%s' % (BUS_LINE)
			print 'Number of Active Buses : %s' % len(busno)
			print 'Bus %s is at latitute %s and longitude %s' % (busno, busLat, busLon)
	
	#print findbusloc(API_KEY, BUS_LINE)
	#not sure if I need the above

if __name__=='__main__':
	findbusloc(sys.argv[1], sys.argv[2])	