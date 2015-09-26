import json
import urllib2
import sys
import csv

if __name__=='__main__':
	#name url and pass arguments from command line
	url = ('http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s') % (sys.argv[1], sys.argv[2])
	
	#saving url in variable 'request'
	request = urllib2.urlopen(url)

	#this line loads it as json file
	data = json.load(request)
	
	#json path to find where bus info is nested
	buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
		
	#open csv and write rows
	with open(sys.argv[3], 'wb') as buscsvfile:
		writer = csv.writer(buscsvfile)
		#fist the column headings
		writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])
			
		for b in buses:
			busLat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
			busLon = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
			if len(b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']) > 0:
				busStop = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
				stopStatus = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
			else:
				busStop = "N/A"
				stopStatus = "N/A"

			#now writing rows
			row = [busLat, busLon, busStop, stopStatus]
			writer.writerow(row)
