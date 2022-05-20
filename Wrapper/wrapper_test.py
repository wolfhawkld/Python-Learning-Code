from time import time, sleep
import logging
from functools import wraps, partial

''' Simple Wrapper with params Demo:
def logger(msg=None):
    def run_time(func):
        def wrapper():
            start = time()
            func()
            sleep(1)
            end = time()
            cost_time = end - start
            print("func {} run time {}".format(msg, cost_time))
        return wrapper
    return run_time


@logger(msg="One")
def fun_one():
    sleep(1)


@logger(msg="Two")
def fun_two():
    sleep(1)


fun_one()
fun_two()
'''


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmessage):
            nonlocal logmsg
            logmsg = newmessage

        return wrapper

    return decorate


logging.basicConfig(level=logging.DEBUG)
@logged(logging.WARNING, "add", "test")
def add(x, y):
    print(x + y)


add.set_level(50)
add(1, 3)
