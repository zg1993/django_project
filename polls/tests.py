# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Question, Choice
from django.utils import timezone
from datetime import datetime, timedelta
# Create your tests here.


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        dt = timezone.now() + timedelta(days=30)
        q = Question(question_text='test furture?', put_date=dt)
        self.assertIs(q.was_published_recently(), False)