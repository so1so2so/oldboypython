#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import multiprocessing


def f(qq):
    print("in child:", qq.qsize())
    qq.put([42, None, 'hello'])

if __name__ == '__main__':
    q = multiprocessing.Queue()
    q.put("test123")
    p = multiprocessing.Process(target=f, args=(q,))
    p.start()
    p.join()
    print("444", q.get_nowait())
    print("444", q.get_nowait())
