from domain_specific_language.settings import RABBITMQ_URI

# importing all the crons
from domain_specific_language.celery_cron import *

# Default settings
CELERY_DEFAULT_QUEUE = 'hackathon'
CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'task.hackathon'
CELERY_IGNORE_RESULT = True
CELERY_TASK_RESULT_EXPIRES = 300  # time in seconds.
# CELERY_IMPORTS = (
#     'bhi.cron', 'ldf.cron', 'recommendations.cron', 'ad_products.cron')
CELERY_ENABLE_UTC = True
USE_TZ = True
CELERY_TIMEZONE = 'Asia/Kolkata'
# Temporary solution for the memory leak
# CELERYD_MAX_TASKS_PER_CHILD = 2

# ttl for events in celery.ev queue
CELERY_EVENT_QUEUE_TTL = 3600

CELERY_QUEUES = {
    'hackathon': {
        'binding_key': 'task.hackathon'
    },
}

BROKER_URL = RABBITMQ_URI
CELERY_RESULT_BACKEND = 'amqp://'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERYD_HIJACK_ROOT_LOGGER = False

# CELERY_ROUTES = {}
