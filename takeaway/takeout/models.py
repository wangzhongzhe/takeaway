# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(default="", max_length=30)
	avatar = models.CharField(default="", max_length=100)
	address = models.CharField(default="", max_length=1000)
	evaluate = models.IntegerField()
	deliveryTime = models.IntegerField()
	income = models.FloatField()

class Commodity(models.Model):
	belong = models.ForeignKey(Restaurant)
	name = models.CharField(default="", max_length=30)
	prize = models.FloatField()

class Customer(models.Model):
	name = models.CharField(default="", max_length=30)
	avatar = models.CharField(default="", max_length=100)
	password = models.CharField(default="", max_length=16)
	address = models.CharField(default="", max_length=1000)
	outcome = models.FloatField()

class Order(models.Model):
	restaurant = models.ForeignKey(Restaurant)
	customer = models.ForeignKey(Customer)
	commodity = models.ForeignKey(Commodity)
	num = models.IntegerField()
	amount = models.FloatField()
	orderTime = models.DateTimeField(auto_now_add=True)