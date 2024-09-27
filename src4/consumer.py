import os
import time
from kafka import KafkaConsumer
from resnet import resnet18
import torch
import json
from pymongo import MongoClient

consumer = KafkaConsumer(bootstrap_servers="192.168.5.33:9092")
consumer.subscribe(topics=["images"])

model = resnet18(pretrained=True)

client = MongoClient('mongodb://192.168.5.116:27017/')
db = client['kafka_db']
collection = db['images']

for msg in consumer:
    print('received')
    message = json.loads(msg.value.decode('utf-8'))

    image_id = message['id']
    data = message['data']
    data = torch.tensor(data).reshape((1,3,32,32)).to(dtype=torch.float32)

    model.eval()

    with torch.no_grad():
        output = model(data)

    _, predicted_class = torch.max(output, 1)

    message['prediction'] = predicted_class.item()

    print(message['label'], message['prediction'])

    collection.update_one(
        {'id': image_id},
        {'$set': message},
        upsert=True
    )


    print('success')

    
    
consumer.close()