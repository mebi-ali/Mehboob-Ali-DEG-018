#!/bin/bash

# This script creates Kafka topics on a broker.

# Create a Kafka topic named 'events' with a bootstrap server on 'broker:9092':
docker compose exec broker kafka-topics --create --topic KafkaTopic1 --bootstrap-server broker:9092

# Create a Kafka topic named 'KafkaAssignment' with 4 partitions and a bootstrap server on 'broker:9092':
docker compose exec broker kafka-topics --create --topic KafkaTopic2 --bootstrap-server broker:9092 --partitions 4

# Create a Kafka topic named 'HelloKafka' with 2 partitions and a bootstrap server on 'broker:9092':
docker compose exec broker kafka-topics --create --topic KafkaTopic3 --bootstrap-server broker:9092 --partitions 2

# List all the Kafka topics with a bootstrap server on 'broker:9092':
docker compose exec broker kafka-topics --list --bootstrap-server broker:9092

# Description of the KafkaTopic2 with a bootstrap server on 'broker:9092':
docker compose exec broker kafka-topics --describe --topic KafkaTopic2 --bootstrap-server broker:9092