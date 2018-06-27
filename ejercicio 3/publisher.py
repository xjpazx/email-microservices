import json
import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type='direct')

channel.basic_publish(exchange='logs',
                      routing_key='error',
                      body=json.dumps({"tipo": "error",
                     "codigo": "codigoXCVBA",
                     "cuerpo": "cuerpo_ejemplo",}))

print "publicado"

connection.close()