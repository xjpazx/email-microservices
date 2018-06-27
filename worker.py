import pika
from enviar import enviar_email
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue="importers")

def importers(ch,method,properties,body):
    j=json.loads(body)
    enviar_email(j['para'],j['asunto'],j['cuerpo'])

channel.basic_consume(importers,queue="importers",no_ack=False)

print "inicio del worker"

channel.start_consuming()