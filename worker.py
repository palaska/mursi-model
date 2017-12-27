import pika
import json
import _mysql

db = _mysql.connect(host="localhost",user="palaska", passwd="1234",db="mydb")

def callback(ch, method, properties, body):
    # print(" [x] Received %r" % body)
    message = json.loads(body)

    if (message['task_type'] == 'read'):
      db.query("SELECT * FROM customers WHERE customer_no=" + message['customer_no'] + " AND date=" + message['date'])
      data = db.store_result()
      data = data.fetch_row()
      print(data)
      # db query
      # run analysis
      # create write task
      ch.basic_ack()
    elif (message['task_type'] == 'write'):
      # write to output db
      ch.basic.ack()
    else:
      ch.basic.nack()

def run():
  connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
  channel = connection.channel()
  channel.queue_declare(queue='task_queue')

  channel.basic_consume(callback,
                        queue='task_queue',
                        no_ack=False)

  print(' [*] Waiting for messages. To exit press CTRL+C')
  channel.start_consuming()
