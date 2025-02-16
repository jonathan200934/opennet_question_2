# RabbitMQ Python Application

A modular Python application demonstrating RabbitMQ message queue implementation with separate producer and consumer components.

## Project Structure

```
rabbitmq-python/
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile            # Docker image configuration
├── requirements.txt      # Python dependencies
├── main.py              # Example implementation
└── rabbitmq/            # Main package directory
    ├── __init__.py      # Package initialization
    ├── base.py          # Base RabbitMQ connection handler
    ├── consumer.py      # Message consumer implementation
    └── producer.py      # Message producer implementation
```

## Components

- **base.py**: Contains the base RabbitMQ connection logic with retry mechanisms and connection management
- **producer.py**: Implements message production functionality
- **consumer.py**: Implements message consumption with support for custom callbacks
- **main.py**: Provides example usage of the producer and consumer modules

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:
```bash
git clone <repository-url>
cd repository
```

2. Start the application using Docker Compose:
```bash
docker-compose up --build
```

This will:
- Build the Python application image
- Start RabbitMQ container with management UI
- Start the Python application container
- Connect the containers using Docker networking

## Accessing RabbitMQ Management UI

The RabbitMQ management interface is available at:
- URL: http://localhost:15672
- Username: guest
- Password: guest

## Environment Variables

- `RABBITMQ_HOST`: RabbitMQ server hostname (default: "localhost")
- `RABBITMQ_DEFAULT_USER`: RabbitMQ username (default: "guest")
- `RABBITMQ_DEFAULT_PASS`: RabbitMQ password (default: "guest")

## Development

To add new features or modify existing ones:

1. The package is modular, so you can extend the base classes or add new ones
2. Ensure to maintain the connection handling patterns from the base class
3. Add appropriate error handling and logging
4. Test your changes both locally and in Docker environment

### GIF Demo
![Kapture 2025-02-16 at 15 44 20](https://github.com/user-attachments/assets/f946ca61-f46c-44c5-b9e4-631ffae7d6f5)

After a few second, it will show the messages sent and received
![Kapture 2025-02-16 at 15 44 20](https://github.com/user-attachments/assets/61513c11-2191-4827-ab04-717b69913732)
