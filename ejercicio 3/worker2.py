import pika
from enviar import enviar_email
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='direct'
)
result=channel.queue_declare(exclusive=True)
queue_name=result.method.queue
channel.queue_bind(exchange='logs',routing_key='error',queue=queue_name)

def importers(ch,method,properties,body):
    j=json.loads(body)
    enviar_email("pazgenes@hotmail.com",j['codigo'],j['tipo'])

channel.basic_consume(importers,queue=queue_name,no_ack=False)

print "inicio del worker2"

channel.start_consuming()