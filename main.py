import math
import json

class DummyGPS:
    def GetLocation(self):
        return (5,5);



str = None
with open('residential.json') as f:
    str = f.read();

j = json.loads(str)

gps = DummyGPS()
#gps = SL4AGPS()

radiusOfNotif = 5

def CheckIfInsideCoordinate(dataX,dataY,gpsX,gpsY,radius):
    d = math.sqrt( (dataX-gpsX)**2 + (dataY-gpsY)**2 )
    if(radius<=d):
        return (True,d)
    return (False,d)


b = CheckIfInsideCoordinate(5,5,10,10,4)
assert(b[0]==True)
b = CheckIfInsideCoordinate(5,5,10,10,10)
assert(b[0]==False)

