import android
droid = android.Android()
droid.webViewShow("/storage/emulated/0/sl4a/scripts/main.html")


import math
import json
import datetime

class DummyGPS: #harvard
    def GetLocation(self):
        return (2463830,1480081);

class DummyGPSUniv: #columbine
    def GetLocation(self):
        return (2447731,1514886);

class NotifySpeak:
    def Notify(self,msg):
        droid.ttsSpeak(msg)

class NotifyPrint:
    def Notify(self,msg):
        print msg

gps = DummyGPS()
# gps = SL4AGPS()



# filename = 'residential.json'
filename = '/storage/emulated/0/sl4a/scripts/residential.json'
str = None
with open(filename) as f:
    str = f.read();

j = json.loads(str)

#iNotifyPrint = NotifyPrint()
iNotifyPrint = NotifySpeak()

def CheckIfInsideCoordinate(dataX,dataY,gpsX,gpsY,radius):
    d = math.sqrt( ((dataX-gpsX)**2) + ((dataY-gpsY)**2) )
    if(radius>=d):
        return (True,d)
    return (False,d)


def CheckIfCurrentDateValid(endDate,startDate,currentYear, estYear, currentMonth):
    if(estYear!=currentYear): return False
    return (startDate<=currentMonth and endDate>=currentMonth)

# unit test
b = CheckIfInsideCoordinate(5,5,10,10,4)
assert(b[0]==False)
b = CheckIfInsideCoordinate(5,5,10,10,10)
assert(b[0]==True)




def jsonDataAlgo(radius):
    ctr =0
    radiusOfNotif = radius
    dtNow = datetime.datetime.now()
    lstFeatures = j['features']

    for lstFeature in lstFeatures:
        #print ctr
        ctr+=1
        prop = lstFeature['properties']
        projStreet = prop['ProjStreet']
        fromStreet=prop['FromStreet']
        SHAPE_Area = prop['SHAPE_Area']
        toStreet =prop['ToStreet']
        year = int(prop['Year'])
        estStart = prop['EstStart']
        estEnd = prop['EstEnd']
        estStartMonthInt = 1
        estEndMonthInt = 12

        if(estStart):
            estStartMonthInt = datetime.datetime.strptime(estStart, '%B').date().month
        if(estEnd):
            estEndMonthInt = datetime.datetime.strptime(estEnd, '%B').date().month
        if(CheckIfCurrentDateValid(estEndMonthInt,estStartMonthInt,dtNow.year,year,dtNow.month)):
            coords = lstFeature['geometry']['coordinates']
            for coord in coords:
                for c in coord:
                    x = c[0]
                    y = c[1]
                    gpsdata = gps.GetLocation()
                    gpsx = gpsdata[0]
                    gpsy = gpsdata[1]

                    b = CheckIfInsideCoordinate(x,y,gpsx,gpsy,radiusOfNotif)
                    if(b[0]):
                        msg = "There is an construction on-going at %s from %s to %s in %.2f miles" % (projStreet, fromStreet,toStreet, b[1])
                        droid.vibrate(1000)
                        iNotifyPrint.Notify(msg)
                        return
            pass


while True:
    result = droid.eventWaitFor('fetch_data').result
    #loc = (resuniv['data'])
    # print "loc is", loc
    # if(loc=='1'): # harvard
    #     gps = DummyGPS()
    # else:#univ st
    #     gps = DummyGPSUniv()

    #gps = DummyGPS()
    gps = DummyGPSUniv()

    radius = int(result['data'])

    if(radius == -1):
        droid.startActivity('android.intent.action.VIEW', 'https://www.google.com/maps/@30.68472,-89.5968968', None,None, False, None, None)
    else:
        jsonDataAlgo(radius)
#   droid.ttsSpeak(result["data"])

print "Done"