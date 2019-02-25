# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    put_date = models.DateTimeField('put_date')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timedelta(days=0) < (timezone.now() - self.put_date) <= timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Field(models.Model):
    name = models.CharField(max_length=100, blank=True)