import os
import time
import json
from kafka import KafkaConsumer
from pymongo import MongoClient

consumer = KafkaConsumer(bootstrap_servers="192.168.5.19:9092")
consumer.subscribe(topics=["images"])

client = MongoClient('mongodb://192.168.5.116:27017/')
db = client['kafka_db'] 
collection = db['images']

for msg in consumer:
    try:
        message = json.loads(msg.value.decode('utf-8'))
        print(message)
        collection.insert_one(message)

    except json.JSONDecodeError:
        print("Received message is not a valid JSON")

consumer.close()