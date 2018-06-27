import pika
import json

connection =pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue="importers")
channel.basic_publish(
    exchange="",
    routing_key="importers",
    body=json.dumps({"para": "pazgenes@hotmail.com",
                     "asunto": "asunto1",
                     "cuerpo": "prueba1",})
)

print "finalizado"

connection.close()