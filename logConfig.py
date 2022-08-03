#!/usr/bin/python
# coding=utf-8
import os
from customTools import chmodPermiss

logDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
logFile = os.path.join(logDir, "alert.log")
chmodPermiss(logDir, 766)

config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
        },
        'simple': {
            'class': 'logging.Formatter',
            'format': '%(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'detailed',
            'level': 'INFO'
        },
        'alertfile': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': logFile,
            # 'mode': 'w', 无该参数
            'formatter': 'detailed',
            'when': 'D',
            'backupCount': 7,
            'encoding': 'utf-8'
        },
    },
    'loggers': {
        'alert': {
            'handlers': ['alertfile'],
            # 'level': 'DEBUG',
            # 'propagate': True
        }
    },
    'root': {
        'handlers': ['console', 'alertfile'],
        'level': 'DEBUG'
    }
}


