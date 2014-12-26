import threading
import time
def clock(interval):
    while True:
        print("The time is %s" % time.ctime())
        time.sleep(interval)
def writer(x, event_for_wait, event_for_set):
    for i in xrange(3):
        event_for_wait.wait()
        event_for_wait.clear()
        print x
        event_for_set.set()

try:
        while True:
                e1 = threading.Event()
                e2 = threading.Event()
                t1 = threading.Thread(target=writer, args=(0, e1, e2))
                t2 = threading.Thread(target=writer, args=(1, e2, e1))
                t = threading.Thread(target=clock, args=(15,))
                t1.start()
                t2.start()
                e1.set()
                t.start()
                time.sleep(2)
except KeyboardInterrupt:
        print "KeyboardInterrupt detected!"
        t1.join()
        t2.join()
        t.join()