# Cloud Computing Project 1 - Structure and Architecture

## Virtual Machine (VM) Architecture

### VM1 - MongoDB Server
- **Database:** MongoDB hosted locally.
- **Database Name:** `kafka_db`
- **Collection Name:** `image`
- **Description:** 
  - VM1 hosts a MongoDB database where the raw images and their metadata are stored.
  - This data originates from our Kafka producer (VM3) and serves as the foundation for further processing and analysis.
  - The `image` collection stores data related to the images from the CIFAR-10 dataset, including any metadata provided by the Kafka producer.

### VM2 - DB Consumer
- **Function:** 
  - This VM serves as a consumer that takes the image from VM3 and sends it to the database
- **Process:** 
  - The data processed on this VM adds to the MongoDB `image` collection
    
### VM3 - Kafka & IoT (Inference) Producer
- **Data Source:** CIFAR-10 dataset.
- **Kafka Role:** 
  - Acts as the producer for Kafka, sending messages containing images to VM2 and VM4.
  - This VM also serves as an IoT inference producer, simulating data streams that push image data for further processing and machine learning prediction.
- **Flow:** 
  - The Kafka producer fetches images from the CIFAR-10 dataset and publishes them to a Kafka topic. These messages are consumed by VM2 and VM4 for inference.

### VM4 - Inference Consumer & ML Model
- **Model:** Resnet-18
- **Role:** 
  - This VM runs the Resnet-18 model to make predictions on the images from the CIFAR-10 dataset.
  - It acts as the inference consumer by processing the image data sent from the Kafka producer on VM3.
- **Flow:** 
  - Images are ingested from the Kafka topic, and the Resnet-18 model makes predictions on these images. The inference results, along with the prediction confidence, are sent to VM1 for storage in MongoDB.

## Technologies
- **MongoDB:** Primary database system for storing and retrieving image data.
- **Kafka:** Message broker for streaming image data across VMs.
- **CIFAR-10 Dataset:** Dataset used for image classification tasks.
- **Resnet-18:** Deep learning model used for making image predictions.
