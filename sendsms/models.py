# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Phone(models.Model):

    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11)
    username = models.CharField(max_length=30)
    verify_code = models.CharField(max_length=6)
    status = models.CharField(max_length=10)
    send_time = models.DateTimeField(default=timezone.datetime.now)

class Email(models.Model):

    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    verify_code = models.CharField(max_length=6)
    status = models.CharField(max_length=10)
    send_time = models.DateTimeField(default=timezone.datetime.now)
