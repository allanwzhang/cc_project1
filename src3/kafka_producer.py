import os
import time
import json
from kafka import KafkaProducer
from sample_image import load_data, sample_image

producers = []
producers.append(KafkaProducer(bootstrap_servers="192.168.5.19:9092", acks=1))
producers.append(KafkaProducer(bootstrap_servers="192.168.5.33:9092", acks=1))

data_folder = '../data/cifar-10-batches-py/'
images, labels, filenames, label_names = load_data(os.path.join(data_folder, 'data.pkl'))

for i in range(1):
    index, image, label, filename = sample_image(images, labels, filenames)
    
    message = {
        "id": index,
        "label": label,
        "label_name": label_names[label].decode('utf-8'),
        "data": image.tolist(),
        "filename": filename
    }

    message_bytes = json.dumps(message).encode('utf-8')
    
    for producer in producers:
        producer.send("images", value=message_bytes)
        producer.flush()
    print(image)
    print(message["data"])

    time.sleep(1)
producer.close()
