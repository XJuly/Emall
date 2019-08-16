# -*- coding:utf-8 -*-
# Author: Jaylen
# date: 2019/8/15

logfile = '../log/access.log'
LOGGING_DIC = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                      '[%(levelname)s][%(message)s]'
        },
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
    },
    'hadlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': logfile,
            'encoding': 'utf-8'

        },
    },
    'loggers': {
        '': {
            'handlers': 'default',
            'level': 'INFO',
            'propagate': True
        },
    },

}
