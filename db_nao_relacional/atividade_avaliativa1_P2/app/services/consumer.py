import json
import time
import sys
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

def callback(ch, method, properties, body):
    """Callback invoked when a message is received"""
    try:
        msg = json.loads(body.decode())
        print(f"Recebido: {msg}", flush=True)
    except json.JSONDecodeError:
        print(f"Recebido (raw): {body.decode()}", flush=True)
    
    # Acknowledge message receipt
    ch.basic_ack(delivery_tag=method.delivery_tag)

def get_connection_parameters():
    """Get RabbitMQ connection parameters with retry settings"""
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    return pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        virtual_host=RABBITMQ_VHOST,
        credentials=credentials,
        connection_attempts=RABBITMQ_CONNECTION_ATTEMPTS,
        retry_delay=RABBITMQ_RETRY_DELAY,
        heartbeat=600
    )

def main():
    """Main consumer loop with reconnection logic"""
    while True:
        try:
            # Setup RabbitMQ connection with retry
            print(f"Conectando ao RabbitMQ ({RABBITMQ_HOST}:{RABBITMQ_PORT})...", flush=True)
            connection = pika.BlockingConnection(get_connection_parameters())
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
            
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Erro de conexão: {str(e)}", flush=True)
            print(f"Tentando novamente em {RABBITMQ_RETRY_DELAY}s...", flush=True)
            time.sleep(RABBITMQ_RETRY_DELAY)
            
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