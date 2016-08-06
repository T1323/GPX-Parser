import xml.etree.ElementTree as et
import numpy as np
import matplotlib.pyplot as plt
import re

class gpx_point():
    def __init__(self, lat, lon, ele, hr):
        self.lat = lat
        self.lon = lon
        self.ele = ele
        self.hr = hr
    def __str__(self):
        return ', '.join([str(self.lat), str(self.lon), str(self.ele), str(self.hr)])

fin = open('..\GPX\RK_gpx _2016-08-02_0601.gpx', 'rt')
gpx_str = fin.read()
m = re.findall(r'gpxtpx=".*"', gpx_str)
gpxtpx = m[0][8:-1]
ns = {'xmlns': 'http://www.topografix.com/GPX/1/1', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'gpxtpx': gpxtpx}

root = et.fromstring(gpx_str)

gpx_point_list = []
for trkpt in root.iter('{http://www.topografix.com/GPX/1/1}trkpt'):
    lat = float(trkpt.get('lat'))
    lon = float(trkpt.get('lon'))
    ele = float(trkpt.find('xmlns:ele', ns).text)
    hr = int(trkpt.find('xmlns:extensions', ns).find('gpxtpx:TrackPointExtension', ns).find('gpxtpx:hr', ns).text)
    point = gpx_point(lat, lon, ele, hr)
    gpx_point_list.append(point)

for p in gpx_point_list:
    print(p)
#ele = [float(trkpt.find('xmlns:ele', ns).text) for trkpt in root.iter('{http://www.topografix.com/GPX/1/1}trkpt')]
#ele_v = np.array(ele)
#plt.plot(ele_v)
#plt.show()

