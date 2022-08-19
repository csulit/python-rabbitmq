import json

from command import cli
from connection import rabbitmq_connect

try:
    c = rabbitmq_connect().channel()

    queue = c.queue_declare('test')
    queue_name = queue.method.queue

    c.queue_bind(
        exchange='kmc',
        queue=queue_name,
        routing_key='kmc.test'
    )

    def callback(ch, method, properties, body):
        payload = json.loads(body)
        print(payload)
        cli()
        ch.basic_ack(delivery_tag=method.delivery_tag)

    c.basic_consume(on_message_callback=callback, queue=queue_name)

    print('[*] Waiting for message.')

    c.start_consuming()

except Exception as e:
    print({'reason': 'RMQ-Process terminate : {}'.format(e)})
