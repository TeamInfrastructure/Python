import android
droid = android.Android()


import math
import json

class DummyGPS:
    def GetLocation(self):
        return (5,5);


filename = 'residential.json'
filename = '/storage/emulated/0/sl4a/scripts/residential.json'
str = None
with open(filename) as f:
    str = f.read();

j = json.loads(str)

gps = DummyGPS()
#gps = SL4AGPS()

radiusOfNotif = 5

def CheckIfInsideCoordinate(dataX,dataY,gpsX,gpsY,radius):
    d = math.sqrt( (dataX-gpsX)**2 + (dataY-gpsY)**2 )
    if(radius>=d):
        return (True,d)
    return (False,d)


b = CheckIfInsideCoordinate(5,5,10,10,4)
assert(b[0]==False)
b = CheckIfInsideCoordinate(5,5,10,10,10)
assert(b[0]==True)

print "Done"