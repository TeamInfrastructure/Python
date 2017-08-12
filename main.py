# import android
# droid = android.Android()


import math
import json
import datetime

class DummyGPS:
    def GetLocation(self):
        return (5,5);


class NotifySpeak:
    def Notify(self,msg):
        droid.ttsSpeak(msg)

class NotifyPrint:
    def Notify(self,msg):
        print msg




filename = 'residential.json'
#filename = '/storage/emulated/0/sl4a/scripts/residential.json'
str = None
with open(filename) as f:
    str = f.read();

j = json.loads(str)

gps = DummyGPS()
#gps = SL4AGPS()

radiusOfNotif = 5
iNotifyPrint = NotifyPrint()
#iNotifyPrint = NotifySpeak()

def CheckIfInsideCoordinate(dataX,dataY,gpsX,gpsY,radius):
    d = math.sqrt( (dataX-gpsX)**2 + (dataY-gpsY)**2 )
    if(radius>=d):
        return (True,d)
    return (False,d)


b = CheckIfInsideCoordinate(5,5,10,10,4)
assert(b[0]==False)
b = CheckIfInsideCoordinate(5,5,10,10,10)
assert(b[0]==True)

dtNow = datetime.datetime.now()
lstFeatures = j['features']
for lstFeature in lstFeatures:
    prop = lstFeature['properties']
    projStreet = prop['ProjStreet']
    year = prop['Year']
    estStart = prop['EstStart']
    estEnd = prop['EstEnd']
    estStartMonthInt = 0
    estEndMonthInt = 0

    if(estStart):
        estStartMonthInt = datetime.datetime.strptime(estStart, '%B').date().month
    if(estEnd):
        estEndMonthInt = datetime.datetime.strptime(estEnd, '%B').date().month


print "Done"