#!/usr/bin/env python
#-*-coding:utf-8-*-
#=======================================
# Author: liuzhida - liuzhia@meituan.com
# Last modified: 2012-08-22 16:24
# Filename: grub.py
# Description:
#=======================================
import helpers
import redis
channel = "kfc"
c = redis.Redis(host='127.0.0.1', port=6379, db=1)
li = c.lrange("dinner:data:%s" % channel, 0, -1)
data = []
for i in li:
    # i = eval(i)
    # i = helpers.json_decode(i)
    print type(i)
    i = helpers.json_decode(i)
    # i = helpers.json_encode(i)
    # print type(i)
    print i
    data.append(i)
#data = helpers.json_encode(data)
# print type(data)
#print data
#print '========'
# with open("%s.list"%channel) as f:
#    a =  f.read()
#    print type(a)
#    print a
'''
{
    "name": "肯德基",
    "content": [
        {
            "category": "cate",
            "dishes": [
                {
                    "name": "name",
                    "price": "price"
                },
                {
                    "name": "name",
                    "price": "price"
                }
            ]
        },
        {
            "category": "cate",
            "dishes": [
                {
                    "name": "name",
                    "price": "price"
                },
                {
                    "name": "name",
                    "price": "price"
                }
            ]
        }
    ]
}
'''
