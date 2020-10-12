import socket
import time

from confluent_kafka import Consumer, Producer

conf = {'bootstrap.servers': "dan-ubu20:9092",
        'client.id': socket.gethostname()}


def acked(err, msg):
    if err:
        print(err)
    else:
        print(msg)


# producer = Producer(conf)
# for i in range(1000):
#     producer.produce('biv-topic1', key='key' + str(i),
#                      value='value', callback=acked)
#     print(i)


time.sleep(1000)
