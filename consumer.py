import pika
from pika import channel

url_params = pika.URLParameters('amqps://aufinhks:PaQoo2lak0mHCXFb3fzEiHy7q7-N2Daq@baboon.rmq.cloudamqp.com/aufinhks')

connection = pika.BlockingConnection(url_params)

channel = connection.channel()

channel.queue_declare(queue='workflow')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='workflow', on_message_callback=callback)

print("Started Consuming")

channel.start_consuming()

channel.close()
