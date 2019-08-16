# -*- coding:utf-8 -*-
# Author: Jaylen
# date: 2019/8/15


import json
import logging.config
from core import src
from conf import setting


def save(user_dic):
    with open('db.json', 'a+') as f:
        json.dump(user_dic, f,ensure_ascii=False)
        f.flush()


def reads():
    with open('db.json') as f:
        user_dic = json.load(f)
        return user_dic


def login_auth(func):
    def wrapper(*args, **kwargs):
        if not src.user_info['name']:
            src.login()
        else:
            return func(*args, **kwargs)

    return wrapper


def get_logger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger

