from .base import RabbitMQBase

class MessageProducer(RabbitMQBase):
    def __init__(self):
        super().__init__()
        self.connect()

    def send_message(self, message: str) -> bool:
        try:
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