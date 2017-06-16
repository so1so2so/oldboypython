#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from multiprocessing import Process, Pool,  freeze_support
import time
import os


def foo(i):
    time.sleep(2)
    print("in process", os.getpid())
    return i + 100


def bar(arg):
    print('-->exec done:', arg,os.getpid())

if __name__ == '__main__':
    #freeze_support()
    pool = Pool(processes=5)  # 允许进程池同时放入5个进程
    print("主进程",os.getpid())
    for i in range(10):
        # pool.apply_async(func=foo, args=(i,), callback=bar)  # callback=回调
        # pool.apply(func=foo, args=(i,)) # 串行
        pool.apply_async(func=foo, args=(i,))  # 并行
    print('end')
    pool.close()
    pool.join()
    # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。.join()