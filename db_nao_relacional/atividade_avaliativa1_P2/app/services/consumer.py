import json
import time
import sys
import pika
from app.core.config import (
    RABBITMQ_HOST,
    RABBITMQ_USER,
    RABBITMQ_PASS,
    RABBITMQ_QUEUE
)

def callback(ch, method, properties, body):
    """Callback invoked when a message is received"""
    try:
        msg = json.loads(body.decode())
        print(f"Recebido: {msg}", flush=True)
    except json.JSONDecodeError:
        print(f"Recebido (raw): {body.decode()}", flush=True)
    
    # Acknowledge message receipt
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    """Main consumer loop with reconnection logic"""
    while True:
        try:
            # Setup RabbitMQ connection
            credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
            parameters = pika.ConnectionParameters(
                host=RABBITMQ_HOST,
                credentials=credentials
            )
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            
            # Ensure queue exists
            channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
            
            # Configure consumer
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(
                queue=RABBITMQ_QUEUE,
                on_message_callback=callback
            )
            
            print("[*] Aguardando mensagens. CTRL+C para sair", flush=True)
            channel.start_consuming()
            
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ não disponível. Tentando novamente em 5s...", flush=True)
            time.sleep(5)
            
        except KeyboardInterrupt:
            print("Consumidor interrompido pelo usuário", flush=True)
            try:
                connection.close()
            except Exception:
                pass
            sys.exit(0)
            
        except Exception as e:
            print(f"Erro inesperado: {e}", flush=True)
            time.sleep(5)

if __name__ == '__main__':
    main()