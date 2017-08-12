import android 
droid = android.Android() 
droid.webViewShow("/storage/emulated/0/sl4a/scripts/main.html")

while True: 
   result = droid.waitForEvent("say").result
   droid.ttsSpeak(result["data"])