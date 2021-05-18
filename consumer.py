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
channel.queue_declare(queue='workflow_csv')


def callback_inserted(ch, method, properties, body):
    print("recived in apiworkflow")


def callback_csv(ch, method, properties, body):
    print('consumed workflow and generate csv')


channel.basic_consume(queue='workflow', on_message_callback=callback_inserted, auto_ack=True, )
channel.basic_consume(queue="workflow_csv", on_message_callback=callback_csv, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
