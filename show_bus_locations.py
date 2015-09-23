import sys
import json
import urllib2

if __name__=='__main__':
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
	request = urllib2.urlopen(url)
	data = json.load(request)
	bus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	num_of_bus = len(bus)
	print 'Bus Line : %s' % sys.argv[2]
	print 'Number of Active Buses : %d' % num_of_bus

	for i in range(num_of_bus):
		lat = bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		lon = bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		print 'Bus %d is at latitude %s and longitude %s' % (i, lat, lon)