# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import sys
import MySQLdb
from django.http import HttpResponse
from takeout.models import *

coon = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", db="takeawaydb", charset="utf8")
cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)

def index(request):
    n = cursor.execute("select * from takeout_restaurant")
    all_resaurant = cursor.fetchall()
    return HttpResponse(json.dumps(all_resaurant))

def insert_new_restaurant(request):
    sql = "insert into takeout_restaurant (name, avatar, address, evaluate, deliveryTime, income) values ('huangmenji', './img/xx.jpg', 'nanyouguangchang', 50, 30, 0)"
    # param = ('huangmenji', './img/xx.jpg', 'nanyouguangchang', 50, 30, 0.0)
    n = cursor.execute(sql)
    coon.commit()
    return HttpResponse("success")

def insert_new_customer(request):
    sql = "insert into takeout_customer (name, avatar, password, address, outcome) values (%s, %s, %s, %s, %f)"
    param = ('xuekai', './img/xx.jpg', '123456', 'Nanjing', 0)
    n = cursor.execute(sql, param)
    coon.commit()
    return HttpResponse("insert success")

def get_or_create_commodity(request):
    if request.method == 'GET':
        sql = "select id from takeout_restaurant where name='huangmenji'"
        n = cursor.execute(sql)
        restaurant_id = cursor.fetchall()[0]['id']
        sql = "select * from takeout_commodity where belong_id=" + str(restaurant_id)
        n = cursor.execute(sql)
        print n
        all_commodity = cursor.fetchall()
        return HttpResponse(json.dumps(all_commodity))
    elif request.method == 'POST':
        commodity_name = ''
        restaurant_id = ''
        prize = ''
        sql = "select * from takeout_commodity where name=" + commodity_name + "and belong_id=" + str(restaurant_id)
        n = cursor.execute(sql)
        if n > 0:
            sql = "update takeout_commodity set prize=" + prize + "where name=" + commodity_name + "and belong_id=" + str(restaurant_id)
        else:
            sql = "insert into takeout_commodity (name, prize, belong_id) values (" + commodity_name + "," + prize + "," + restaurant_id + ")"
        n = cursor.execute(sql)
        coon.commit()
        return HttpResponse("success")
