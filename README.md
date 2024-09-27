# Cloud Computing Project 1 - Database Structure and Architecture

## Overview
This document provides an overview of the database and associated components structure for Cloud Computing Project 1. Our infrastructure is organized to handle data ingestion, processing, and machine learning inference using the CIFAR-10 dataset and the Resnet-18 model.

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
  - This VM serves as a database consumer that augments the data within the `kafka_db` database.
  - It adds **truth values** (ground truth labels) and any additional augmented data related to the images.
- **Process:** 
  - The data processed on this VM updates the MongoDB `image` collection by appending the necessary labels and metadata that are required for inference and evaluation.

### VM3 - Kafka & IoT (Inference) Producer
- **Data Source:** CIFAR-10 dataset.
- **Kafka Role:** 
  - Acts as the producer for Kafka, sending messages containing images and related metadata to VM1 for storage in MongoDB.
- **IoT Inference:** 
  - This VM also serves as an IoT inference producer, simulating data streams that push image data for further processing and machine learning prediction.
- **Flow:** 
  - The Kafka producer fetches images from the CIFAR-10 dataset and publishes them to a Kafka topic. These messages are consumed by VM4 for inference.

### VM4 - Inference Consumer & ML Model
- **Model:** Resnet-18
- **Role:** 
  - This VM runs the Resnet-18 model to make predictions on the images from the CIFAR-10 dataset.
  - It acts as the inference consumer by processing the image data sent from the Kafka producer on VM3.
- **Flow:** 
  - Images are ingested from the Kafka topic, and the Resnet-18 model makes predictions on these images. The inference results, along with the prediction confidence, are sent back to VM2 for storage in MongoDB.

## Data Flow Overview
1. **VM3 (Kafka Producer)** sends image data from the CIFAR-10 dataset to the MongoDB `image` collection on **VM1**.
2. **VM2 (DB Consumer)** adds augmented data, such as truth labels, to the existing records in the `image` collection.
3. The **Resnet-18 model on VM4** consumes the image data and makes predictions.
4. Inference results are stored back in MongoDB for further analysis and evaluation.

## Key Technologies
- **MongoDB:** Primary database system for storing and retrieving image data.
- **Kafka:** Message broker for streaming image data across VMs.
- **CIFAR-10 Dataset:** Dataset used for image classification tasks.
- **Resnet-18:** Deep learning model used for making image predictions.

## Future Enhancements
- Automating the process of inference and result storage.
- Expanding the dataset to include additional categories for image classification.
- Implementing additional monitoring and logging for better tracking of data and inference results.

---

This setup allows us to efficiently manage and process large volumes of image data, ensuring smooth communication between components and reliable prediction outcomes for Cloud Computing Project 1.
