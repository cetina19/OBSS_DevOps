import pika

credentials = pika.PlainCredentials('alper', 'alper1234')

connection_parameters = pika.ConnectionParameters(host='localhost',port=5672,virtual_host='/',credentials=credentials)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='NewQueue')

message = "Hello from Alper!"

channel.basic_publish(exchange='', routing_key='NewQueue', body=message)

print(f"sent message {message}")

connection.close()