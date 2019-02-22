# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def index(request, *args, **kwargs):
    print request
    print args
    print kwargs
    return HttpResponse('hello world!')

# Create your views here.
