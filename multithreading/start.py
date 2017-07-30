# coding: utf8

import threading
import time


num = 0
lock = threading.Lock()
def target(s):
    print 'The current threading {} is running sleep'.format(
        threading.current_thread().name)
    print 'sleep {}'.format(s)
    print 'the current threading {} is ended'.format(
        threading.current_thread().name)
    global num
    for i in range(10000):
        lock.acquire()
        try:
            num += s
            num -= s
        finally:
            lock.release()
    print 'result :', num

print 'the current threading {} is running'.format(
    threading.current_thread().name)

r = threading.Thread(target=target, args=[5])
s = threading.Thread(target=target, args=[3])
t = threading.Thread(target=target, args=[2])

t.start()
s.start()
r.start()
t.join()
s.join()
r.join()
print 'the current trreading {} is ended'.format(
    threading.current_thread().name
)
