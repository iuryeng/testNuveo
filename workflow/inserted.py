import json

import pika

params = pika.URLParameters('amqps://aufinhks:PaQoo2lak0mHCXFb3fzEiHy7q7-N2Daq@baboon.rmq.cloudamqp.com/aufinhks')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='workflow', body="inserido na fila")
    print(" [X] enviado para a fila")

def consuming():
    channel.basic_publish(exchange='', routing_key='workflow_csv', body="workflow consumido")
    print(" [X] consumido")