import android 
droid = android.Android() 
droid.webViewShow("/storage/emulated/0/sl4a/scripts/main.html")

while True:
   result = droid.eventWaitFor('fetch_data').result
   print  result
#   droid.ttsSpeak(result["data"])

