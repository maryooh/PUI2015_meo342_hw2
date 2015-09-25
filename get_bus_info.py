import json
import urllib2
import sys
import csv

if __name__=='__main__':
	#defining function that will use the two arguments on the command line
	getbusinfo(sys.argv[1], sys.argv[2])	
	
	#to look at different bus lines, we can change the kame in BUS_LINE
	API_KEY = '9c0690a6-de1f-48a4-ab8c-8db536692b7d'
	BUS_LINE = 'B52'
	
	def getbusinfo(API_KEY, BUS_LINE):
		url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + API_KEY +
		'&VehicleMonitoringDetailLevel=calls&LineRef=' + BUS_LINE
		data = json.load(open(url,'r'))
		buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['MonitoredVehicleJourney'][0]
		['OnwardCalls']['OnwardCall']['Extensions']
		
		#open csv and write rows
		with open(sys.argv[3], 'wb') as buscsvfile:
			writer = csv.writer(buscsvfile)
			writer.writerow('Latitude','Longitude','Stop Name','Stop Status'])
			
			for b in buses:
				if b ['PublishedLineName'] == BUS_LINE:
					busLat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
					busLon = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
					if len(bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']) > 0:
						busStop = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
						[0]['StopPointName']
						stopStatus = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
						[0]['Extensions']['Distances']['PresentableDistance']
					else:
						busStop = "N/A"
						stopStatus = "N/A"
					row = [busLat, busLon, busStop, stopStatus]
					writer.writerow(row)busStop = b['MonitoredVehicleJourney']['OnwardCalls']
					['OnwardCall'][0]['StopPointName']
					stopstatus= b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
					[0]['Extensions']['Distances']['PresentableDistance']
