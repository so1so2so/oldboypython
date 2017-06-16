#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello from child1'])
    conn.send([42, None, 'hello from child2'])
    print conn.recv()
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print("parent", parent_conn.recv())  # prints "[42, None, 'hello']"
    print("parent", parent_conn.recv())  # prints "[42, None, 'hello']"
    parent_conn.send("发送的儿子的消息")  # prints "[42, None, 'hello']"
    p.join()