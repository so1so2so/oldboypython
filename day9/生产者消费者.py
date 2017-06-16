#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "Alex Li"

import threading, time
import Queue

q = Queue.Queue(maxsize=10)


def producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print("生产了骨头",count)
        count +=1
        time.sleep(1)


def consumer(name):
    #while q.qsize()>0:
    while True:
        print("[%s] 取到[%s] 并且吃了它..." %(name, q.get()))
        time.sleep(1)


p = threading.Thread(target=producer, args=("Alex",))
c = threading.Thread(target=consumer, args=("ChengRonghua",))
c1 = threading.Thread(target=consumer, args=("王森",))
p.start()
c.start()
c1.start()
