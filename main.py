from rabbitmq.producer import MessageProducer
from rabbitmq.consumer import MessageConsumer

def main():
    producer = MessageProducer()
    producer.send_message("Hello World!")

    consumer = MessageConsumer()
    consumer.receive_messages()

if __name__ == "__main__":
    main()