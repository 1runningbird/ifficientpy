# coding: utf8
import functools
import threading

def singleton(cls):
    instance = {}
    @functools.wraps(cls)
    def getinstance(*args, **kargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)
        return instance[cls]
    return getinstance

@singleton
class A(object):
    pass

def getinstance():
    s = A()
    print id(s)

def main():
    while True:
        t = threading.Thread(target=getinstance)
        t.start()


if __name__ == '__main__':
    main()
