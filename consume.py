import pika
import time

credentials = pika.PlainCredentials("testuser1", "testuser1")

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials ))

channel = connection.channel()
channel.queue_declare(queue='test1', durable=True)


def callback(ch, method, properties, body):

    p = properties.headers["filename"]

    f = open(p, "wb") 
    f.write(body)
    f.close()

    print(" [x] Received {}", format(p))

channel.basic_consume(queue='test1', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()