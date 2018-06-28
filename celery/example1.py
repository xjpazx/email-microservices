from celery import Celery
from enviar import enviar_email


app=Celery("example1",backend="amqp://guest:guest@localhost",
           broker="amqp://localhost")

#@app.task
#def add(x,y):
 #   return x+y

@app.task
def send(p,a,c):
    enviar_email(p,a,c)

