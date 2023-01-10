

import pika

path = "some_path"
filename = "test.txt"

with open(path + filename, "rb") as b:
  bo = b.read()


credentials = pika.PlainCredentials("testuser1", "testuser1")

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',credentials=credentials ))
channel = connection.channel()
channel.queue_declare(queue='test1',durable=True)
channel.basic_publish(exchange='', routing_key='test1', properties=pika.BasicProperties(delivery_mode = 2, headers={"filename": filename}), body=bo)

print(" [x] Sent 'Hello World!'")

connection.close()
