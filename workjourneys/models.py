# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Workjourneys(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    schedule = models.CharField(max_length=200)

# Create your models here.
