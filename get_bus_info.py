import sys
import json
import urllib2
import csv

if __name__=='__main__':
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
	request = urllib2.urlopen(url)
	data = json.load(request)
	bus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

	with open(sys.argv[3], 'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])

		for b in bus:
			lat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
			lon = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
			if b['MonitoredVehicleJourney']['OnwardCalls'] != {}:
				sname = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
				sstatus = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
			else:
				sname = 'N/A'
				sstatus = 'N/A'
			#print '%s,%s,%s,%s' % (lat,lon,sname,sstatus)
			writer.writerow([lat,lon,sname,sstatus])