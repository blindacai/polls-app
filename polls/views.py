# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    # render returns an HttpResponse object of the given template rendered with the given context
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    details = "You're looking at question %s." % question_id
    context = {'details': details}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)