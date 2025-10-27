import json
import pika
from app.core.config import (
    RABBITMQ_HOST,
    RABBITMQ_USER,
    RABBITMQ_PASS,
    RABBITMQ_QUEUE
)

async def publish_message(payload: dict):
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        credentials=credentials
    )
    
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    
    # Declare queue (idempotent - won't create if exists)
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    
    # Publish message
    channel.basic_publish(
        exchange='',
        routing_key=RABBITMQ_QUEUE,
        body=json.dumps(payload).encode('utf-8')
    )
    
    connection.close()