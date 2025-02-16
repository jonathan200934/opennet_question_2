from .base import RabbitMQBase

class MessageConsumer(RabbitMQBase):
    def __init__(self):
        super().__init__()
        self.connect()

    def callback(self, ch, method, properties, body: bytes) -> None:
        print(f" [x] Received {body.decode()}")

    def receive_messages(self) -> None:
        try:
            self.channel.basic_consume(
                queue=self.queue_name,
                on_message_callback=self.callback,
                auto_ack=True
            )
            print(' [*] Waiting for messages. To exit press CTRL+C')
            self.channel.start_consuming()

        except KeyboardInterrupt:
            print("\nStopping consumer...")

        except Exception as e:
            print(f"Error receiving messages: {e}")

        finally:
            self.close_connection()