import _mysql
import json
import pika
import worker

def pushToQueue(tuple):
  message = { 'customer_no': tuple[0], 'date': tuple[1], 'task_type': 'read' }
  print("pushing to queue")
  print(message)
  channel.basic_publish(exchange='', routing_key='task_queue', body=json.dumps(message))

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')

db = _mysql.connect(host="localhost",user="palaska", passwd="1234",db="mydb")
# print(db)

db.query("""SELECT DISTINCT customer_no, date FROM customers""")
data = db.store_result()

fetched = data.fetch_row()
while fetched:
  pushToQueue(fetched[0])
  fetched = data.fetch_row()
  pass

connection.close()

for x in xrange(1,4):
  worker.run()
  pass
