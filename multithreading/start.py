# coding: utf8

import threading
import time


def target():
    print 'The current threading {} is running'.format(
        threading.current_thread().name)
    time.sleep(1)
    print 'the current threading {} is ended'.format(
        threading.current_thread().name)

print 'the current threading {} is running'.format(
    threading.current_thread().name)

t = threading.Thread(target=target)

t.start()
t.join()
print 'the current trreading {} is ended'.format(
    threading.current_thread().name
)
