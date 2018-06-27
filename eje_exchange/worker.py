import json
import os

import pika
connection =pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel=connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

results=channel.queue_declare(exclusive=True)
queue_name=results.method.queue# traigo el nombre exclusivo
channel.queue_bind(exchange='logs',queue=queue_name)#bind es la coneccion entre un exchange y una queue
print '[*] Startin worker With queue {}'.format(queue_name)

def callback(ch,method,properties, body):
    j = json.loads(body)
    a=[j['tipo'],j['codigo'],j['cuerpo']]
    b = " ".join(a)

    file=open("archive.txt","a")
    file.write(b)
    file.close()

channel.basic_consume(callback,queue=queue_name,no_ack=False)
channel.start_consuming()