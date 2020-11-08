from kafka import KafkaProducer
import json

bootstrap_servers = ["localhost:9091", "localhost:9092", "localhost:9093"]
topicName = "water3"

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

# String example
# producer.send(topicName, b"Hello World 2!")

# Dictionary example
transaction = {"message": "who won the election?", "answer": "biden"}
message = json.dumps(transaction)

producer.send(topicName, value=message.encode())

producer.flush()