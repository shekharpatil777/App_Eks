import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'detailed': {
            'format': '%(asctime)s %(name)s %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'detailed'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
logging.info("Logging using dictConfig")
