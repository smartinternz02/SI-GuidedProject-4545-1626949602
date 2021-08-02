import wiotp.sdk.device
import time
import random
import json
import requests
myConfig = { 
    "identity": {
        "orgId": "8afe2a",
        "typeId": "IOTCHETAN",
        "deviceId":"11042002"
    },
    "auth": {
        "token": "Chetan@12344321"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,100)
    hum=random.randint(0,100)
    air=random.randint(0,500)
    if temp>80:
        A=requests.get("https://www.fast2sms.com/dev/bulkV2?authorization=g2lTCn6fZ8v5cxOokr7SEFWJ09QzjLYqRbAweHNMspaBP3KVmdhaHRrnWjk8dwSNy7OQKLslgATqiXb0&route=q&message=TEMPERATURE%20LEVEL%20ALERT!%0A&language=english&flash=0&numbers=8837887295")

    name= "PROJECT CARGO"
    #in area location
    latitude= 28.620071
    longitude= 77.049599
    #out area location
    #latitude= 28.620561
    #longitude= 77.052143
    myData= {'name': name, 'lat ':latitude,'lon':longitude, 'temp':temp, 'hum':hum, 'air':air}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0 , onPublish=None)
    print ("Data published to IBM IoT platfrom : ",myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
