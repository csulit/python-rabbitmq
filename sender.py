import json

from connection import channel

c = channel()

c.basic_publish(
    exchange='kmc',
    routing_key='kmc.test',
    body=json.dumps({'body': 'test'}),
)

c.close()
