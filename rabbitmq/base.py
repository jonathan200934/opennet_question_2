import pika
import sys
import time
import os

class RabbitMQBase:
    def __init__(self, queue_name: str = 'test_queue'):
        self.host = os.getenv('RABBITMQ_HOST', 'rabbitmq')
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