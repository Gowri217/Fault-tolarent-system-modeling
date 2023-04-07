from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import datasource as ds

client=AWSIoTMQTTClient("new_Client")
client.configureEndpoint('',8883)
client.configureCredentials("AmazonRootCA1.pem", "device1-private.pem.key","device1-certificate.pem.crt")

client.configureOfflinePublishQueueing(-1) # Infinite Publish Queueing
client.configureDrainingFrequency(2) # Frequency of Data Transfer
client.configureConnectDisconnectTimeout(10) # 10 Seconds
client.configureMQTTOperationTimeout(5) # 5 Seconds

def notification(client,userdata,message):
	print ('Received a new message: ')
	print (message.payload)
	print ("from topic: ")
	print (message.topic)

client.connect() # Try to connect with AWS IoT Core by using above credentials
print ("MQTT Client is connected to AWS IoT Core")
time.sleep(2)
client.subscribe("A12/data",1,notification)

while True:
	payload=ds.dataSource()
	print (payload)
	client.publish('A12/data',payload,0)
	time.sleep(2)