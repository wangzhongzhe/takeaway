# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from takeout.models import Restaurant, Commodity, Customer, Order
admin.site.register([Restaurant, Commodity, Customer, Order])