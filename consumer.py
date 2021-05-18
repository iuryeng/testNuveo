import json
import os
from urllib import request

import pika

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apiworkflow.settings")
django.setup()

from workflow.models import Workflow

url_params = pika.URLParameters('amqps://aufinhks:PaQoo2lak0mHCXFb3fzEiHy7q7-N2Daq@baboon.rmq.cloudamqp.com/aufinhks')

connection = pika.BlockingConnection(url_params)

channel = connection.channel()

channel.queue_declare(queue='workflow')


def callback(ch, method, properties, body):
        print("recived in apiworkflow")


channel.basic_consume(queue='workflow', on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
