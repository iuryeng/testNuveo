import pika

params = pika.URLParameters('amqps://aufinhks:PaQoo2lak0mHCXFb3fzEiHy7q7-N2Daq@baboon.rmq.cloudamqp.com/aufinhks')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(met):
    channel.basic_publish(exchange='', routing_key='workflow', body=' hello recebido da fila!')