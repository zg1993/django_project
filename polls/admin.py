# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['put_date', 'question_text']
    list_display = ('question_text', 'put_date', 'was_published_recently')
    list_filter = ['put_date']
    search_fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['put_date']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)