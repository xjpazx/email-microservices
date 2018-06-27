import pika
from enviar import enviar_email
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)
result=channel.queue_declare(exclusive=True)
queue_name=result.method.queue
channel.queue_bind(exchange='logs',queue=queue_name)

def importers(ch,method,properties,body):
    j=json.loads(body)
    if(j['tipo']=='error'):
        enviar_email("pazgenes1@gmail.com",j['codigo'],j['tipo'])

channel.basic_consume(importers,queue=queue_name,no_ack=False)

print "inicio del worker2"

channel.start_consuming()