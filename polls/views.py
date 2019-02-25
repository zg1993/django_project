# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
import traceback


# Create your views here.
def index(request, *args, **kwargs):
    latest_question_list = Question.objects.order_by('-put_date')[:5]
    # template = loader.get_template('polls/index.html')
    content = {'latest_question_list': latest_question_list}
    # print template.render(content, request)
    return render(request, 'polls/index.html', content)
    # return HttpResponse(template.render(content, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = Choice.objects.get(pk=request.POST['choice'])
    except (Choice.DoesNotExist, KeyError) as e:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice.',
        })
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))