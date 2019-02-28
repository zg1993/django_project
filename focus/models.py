# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=False)


class Author(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    register_date = models.DateTimeField()
    profile = models.TextField()
    favorites = models.ManyToManyField(User,
                                       through='Favorite',
                                       through_fields=('author', 'user'))


class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    put_date = models.DateTimeField()
    update_time = models.DateTimeField()
    author = models.ForeignKey(Author)
    polls = models.ManyToManyField(User,
                                   through='Poll',
                                   through_fields=('article', 'user'),
                                   related_name='poll_users')
    favorites = models.ManyToManyField(User,
                                       through='Favorite',
                                       through_fields=('article', 'user'),
                                       related_name='favorite_users')
    num_comments = models.IntegerField(default=0)
    num_polls = models.IntegerField(default=0)
    num_favotites = models.IntegerField(default=0)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    content = models.TextField()
    put_date = models.DateTimeField()
    poll_num = models.IntegerField(default=0)
    polls = models.ManyToManyField(User,
                                   through='Poll',
                                   through_fields=('comment', 'user'),
                                   related_name='poll_user')


class Poll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField()

