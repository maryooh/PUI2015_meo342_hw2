import json
import urllib2
import sys

if __name__ == '__main__':
	getbusinfo(sys.argv[1], sys.argv[2])	

	API_KEY = '9c0690a6-de1f-48a4-ab8c-8db536692b7d'
	BUS_LINE = 'B52'
	
	def getbusinfo(API_KEY, BUS_LINE):
		url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + API_KEY +'&VehicleMonitoringDetailLevel=calls&LineRef=' + BUS_LINE
		data = json.load(open(url,'r'))
		buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['MonitoredVehicleJourney'][0]['OnwardCalls']['OnwardCall']['Extensions']

		for b in buses:
			if b ['PublishedLineName'] == BUS_LINE:
				busno = b['vehicleref'][10:]
				busLat = b['Latitude']
				busLon = b['Longitude']
				stopname = b['StopPointName']
				stopstatus= b['PresentableDistance']

				print 'Latitude, Longitude, Stop Name, Stop Status'
				print '%s, %s, %s, %s' % (busLat, busLon, stopname, stopstatus)
