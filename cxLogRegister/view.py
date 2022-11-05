#coding=utf-8
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'hello'
    context['world'] = 'world'
    return render(request, 'hello.html', context)


def index(request):
    context = {}
    return render(request, 'index.html', context)

