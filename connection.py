import pika


def rabbitmq_connect():
    param = pika.ConnectionParameters(host='localhost')
    connection = pika.BlockingConnection(param)

    try:
        return connection

    except Exception as e:
        print(({'reason': 'RMQ-Connection-Process terminate : {}'.format(e)}))

def channel():
    channel = rabbitmq_connect().channel()

    channel.exchange_declare(
        exchange='kmc',
        exchange_type='direct',
        durable=True
    )

    return channel

