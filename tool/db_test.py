#!/usr/bin/env python3
#coding:utf-8


import pymongo

host = 'loaclhost'

connection = pymongo.MongoClient("mongodb://%s:27017"%(host))
db = connection.pouchShema
pouchShema = db.pouchShema

dic = {'rebuy_percent': 20,
    'popularity': 20,
    'name': '위치헤이즐 허벌 익스트랙트 토너',
    'vendor_url':'http://shopping.naver.com/search/all.nhn?query=%EC%9C%84%EC%B9%98%ED%97%A4%EC%9D%B4%EC%A6%90+%ED%97%88%EB%B2%8C+%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9E%99%ED%8A%B8+%ED%86%A0%EB%84%88',
    'brand_name': '빌리프',
    'photo_url': 'http://d9vmi5fxk1gsw.cloudfront.net/home/glowmee/upload/20170105/1483596672157.png',
    'category': '토너',
    'product_id': 4303,
    'review_count': 200}

pouchShema.insert(dic)