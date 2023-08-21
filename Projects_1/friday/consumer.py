import pika

def on_message_received(ch, method, properties, body):
    print(f"received new message: {body}")

credentials = pika.PlainCredentials('alper', 'alper1234')

connection_parameters = pika.ConnectionParameters(host='localhost',port=5672,virtual_host='/',credentials=credentials)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='NewQueue')

channel.basic_consume(queue='NewQueue', auto_ack=True, on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()