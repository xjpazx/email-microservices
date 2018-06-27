import json
import sys
import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or 'info: hello world'

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=json.dumps({"tipo": "debug",
                     "codigo": "codigoXCVBA",
                     "cuerpo": "cuerpo",}))

print "publicado"

connection.close()