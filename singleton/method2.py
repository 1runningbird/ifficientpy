# coding: utf8
import threading

Lock = threading.Lock()
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kargs):
        if not cls._instance:
            try:
                Lock.acquire()
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kargs)
            finally:
                Lock.release()
        return cls._instance


def main():
    t = Singleton()
    s = Singleton()
    print id(t), id(s)

def singletontest():
    s = Singleton()
    print id(s)

def main2():
    while True:
        t = threading.Thread(target=singletontest)
        t.start()

if __name__ == '__main__':
    main()
    main2()
