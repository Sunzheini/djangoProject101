from django.shortcuts import render
from django import http
from djangoProject101.task.models import Task


def show_bare_minimum_view(request):
    return http.HttpResponse('It works')


def show_all_tasks(request):
    all_tasks = Task.objects.all()
    result = ', '.join(f"{t.name}({t.id})" for t in all_tasks)
    return http.HttpResponse(result)


def index(request):
    all_tasks = Task.objects.all()
    context = {
        'title': 'The Task App!',
        'tasks': all_tasks
    }
    return render(request, 'index.html', context)

