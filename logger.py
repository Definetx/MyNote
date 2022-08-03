from functools import wraps
import inspect
import logging
import logging.config
import logging.handlers
from logConfig import config
logging.config.dictConfig(config)

def logger(level):
    def decorate(func):
        log = logging.getLogger("%s.%s" % (func.__module__, func.__name__))
        msg = {
            "state": "",
            "args": "",
            "kwargs": "",
            "result": "",
        }
    
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg["state"], msg["args"], msg["kwargs"] = "start", args, kwargs

            log.log(level, msg)
            try:
                result = func(*args, **kwargs)
                msg["state"] = "finsh"
            except Exception as err:
                result = err
                msg["state"] = "error"

            msg["result"] = result
            log.log(level, msg)

            return result
        return wrapper
    return decorate

# @logger(logging.DEBUG)
# def add(x, y):
#     inspect_stack = inspect.stack()[0]
#     log = logging.getLogger("%s.%s" % (inspect_stack.filename, inspect_stack.function))
#     logging.info("%s" % "")
#     return x + y
# 
# a = add(1,2)
# print(a)
 
