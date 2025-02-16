import pika
import sys
import time
import os
from typing import Optional

class RabbitMQHandler:
    def __init__(self, queue_name: str = 'test_queue'):
        self.host = os.getenv('RABBITMQ_HOST', 'localhost')
        self.queue_name = queue_name
        self.connection = None
        self.channel = None
        self.max_retries = 5
        self.retry_delay = 5

    def connect(self) -> None:
        for attempt in range(self.max_retries):
            try:
                parameters = pika.ConnectionParameters(
                    host=self.host,
                    credentials=pika.PlainCredentials(
                        username='guest',
                        password='guest'
                    ),
                    connection_attempts=3,
                    retry_delay=5
                )
                self.connection = pika.BlockingConnection(parameters)
                self.channel = self.connection.channel()
                self.channel.queue_declare(queue=self.queue_name)
                print(f" [*] Successfully connected to RabbitMQ at {self.host}")
                return
            except Exception as e:
                print(f"Connection attempt {attempt + 1} failed: {e}")
                if attempt < self.max_retries - 1:
                    print(f"Retrying in {self.retry_delay} seconds...")
                    time.sleep(self.retry_delay)
                else:
                    print("Max retries reached. Exiting...")
                    sys.exit(1)

    def close_connection(self) -> None:
        if self.connection:
            self.connection.close()

    def send_message(self, message: str) -> bool:
        try:
            self.connect()
            self.channel.basic_publish(
                exchange='',
                routing_key=self.queue_name,
                body=message
            )
            print(f" [x] Sent '{message}'")
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False
        finally:
            self.close_connection()

    def callback(self, ch, method, properties, body: bytes) -> None:
        print(f" [x] Received {body.decode()}")

    def receive_messages(self, timeout: Optional[int] = None) -> None:
        try:
            self.connect()
            self.channel.basic_consume(
                queue=self.queue_name,
                on_message_callback=self.callback,
                auto_ack=True
            )
            print(' [*] Waiting for messages. To exit press CTRL+C')
            if timeout:
                start_time = time.time()
                while time.time() - start_time < timeout:
                    self.connection.process_data_events(time_limit=1)
            else:
                self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()
            print("\nStopping consumer...")
        except Exception as e:
            print(f"Error receiving messages: {e}")
        finally:
            self.close_connection()

def main():
    handler = RabbitMQHandler()
    handler.send_message("Hello, World!")
    handler.receive_messages(timeout=30)

if __name__ == "__main__":
    main()