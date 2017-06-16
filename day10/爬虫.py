#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "Alex Li"

from gevent import monkey
# monkey.patch_all()
# import gevent
# from  urllib.request import urlopen
# import time
import gevent
import urllib
import time
def f(url):
    print('GET: %s' % url)
    resp = urllib.urlopen(url)
    data = resp.read()
    with open('lest.html', 'wb')as s :
        s.write(data)
    print('%d bytes received from %s.' % (len(data), url))

urls = ['https://www.python.org/',
         'https://www.yahoo.com/',
         'https://github.com/'
         ]

# time_start = time.time()
# for url in urls:
#     f(url)
# print("同步cost",time.time() - time_start)

async_time_start = time.time()
gevent.joinall([
    # gevent.spawn(f, 'http://www.panda.tv/'),
    gevent.spawn(f, 'http://www.douyu.com/chenyifaer'),
    gevent.spawn(f, 'https://github.com/'),
])
print("异步cost", time.time()-async_time_start )