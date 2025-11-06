import json
import time
import pika
from app.core.config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASS,
    RABBITMQ_VHOST,
    RABBITMQ_QUEUE,
    RABBITMQ_CONNECTION_ATTEMPTS,
    RABBITMQ_RETRY_DELAY
)

async def publish_message(payload: dict):
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        virtual_host=RABBITMQ_VHOST,
        credentials=credentials,
        connection_attempts=RABBITMQ_CONNECTION_ATTEMPTS,
        retry_delay=RABBITMQ_RETRY_DELAY,
        heartbeat=600
    )
    
    for attempt in range(RABBITMQ_CONNECTION_ATTEMPTS):
        try:
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            
            # Declare queue (idempotent - won't create if exists)
            channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
            
            # Publish message with persistence
            channel.basic_publish(
                exchange='',
                routing_key=RABBITMQ_QUEUE,
                body=json.dumps(payload).encode('utf-8'),
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                    content_type='application/json'
                )
            )
            
            connection.close()
            return
            
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Tentativa {attempt + 1} falhou: {str(e)}")
            if attempt + 1 < RABBITMQ_CONNECTION_ATTEMPTS:
                time.sleep(RABBITMQ_RETRY_DELAY)
            else:
                raise