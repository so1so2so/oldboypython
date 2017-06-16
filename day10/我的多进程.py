#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import multiprocessing
import time


def run(name):
    print "我的名字是张%s" % name
    time.sleep(2)

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run, args=('%s' % i,))
        p.start()
        p.join(20)
        print p.ident