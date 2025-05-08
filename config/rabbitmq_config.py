import os

rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_username = os.getenv('RABBITMQ_DEFAULT_USER')
rabbitmq_password = os.getenv('RABBITMQ_DEFAULT_PASS')

rabbitmq_models_max_retry_number = int(os.getenv('RABBITMQ_MODELS_MAX_RETRY_NUMBER'))
rabbitmq_models_retry_delay_ms = int(os.getenv('RABBITMQ_MODELS_RETRY_DELAY_MS'))
rabbitmq_requests_exchange_name = os.getenv('RABBITMQ_REQUESTS_EXCHANGE_NAME')
rabbitmq_models_queues_dlx_name = os.getenv('RABBITMQ_MODELS_QUEUES_DLX_NAME')
rabbitmq_models_retry_queue_name = os.getenv('RABBITMQ_MODELS_RETRY_QUEUE_NAME')
rabbitmq_models_retry_queue_dlx_name = os.getenv('RABBITMQ_MODELS_RETRY_QUEUE_DLX_NAME')
rabbitmq_results_exchange_name = os.getenv('RABBITMQ_RESULTS_EXCHANGE_NAME')

if rabbitmq_host is None:
    raise ValueError('You should specify RABBITMQ_HOST to be able to connect to RabbitMQ.')

if rabbitmq_username is None:
    raise ValueError('You should specify RABBITMQ_USERNAME to be able to connect to RabbitMQ.')

if rabbitmq_password is None:
    raise ValueError('You should specify RABBITMQ_PASSWORD to be able to connect to RabbitMQ.')

if rabbitmq_models_max_retry_number is None:
    raise ValueError('You should specify RABBITMQ_MODELS_MAX_RETRY_NUMBER to be able to connect to RabbitMQ.')

if rabbitmq_models_retry_delay_ms is None:
    raise ValueError('You should specify RABBITMQ_MODELS_RETRY_DELAY_MS to be able to connect to RabbitMQ.')

if rabbitmq_requests_exchange_name is None:
    raise ValueError('You should specify RABBITMQ_REQUESTS_EXCHANGE_NAME to be able to connect to RabbitMQ.')

if rabbitmq_models_queues_dlx_name is None:
    raise ValueError('You should specify RABBITMQ_MODELS_QUEUES_DLX_NAME to be able to connect to RabbitMQ.')

if rabbitmq_models_retry_queue_name is None:
    raise ValueError('You should specify RABBITMQ_MODELS_RETRY_QUEUE_NAME to be able to connect to RabbitMQ.')

if rabbitmq_models_retry_queue_dlx_name is None:
    raise ValueError('You should specify RABBITMQ_MODELS_RETRY_QUEUE_DLX_NAME to be able to connect to RabbitMQ.')

if rabbitmq_results_exchange_name is None:
    raise ValueError('You should specify RABBITMQ_RESULTS_EXCHANGE_NAME to be able to connect to RabbitMQ.')