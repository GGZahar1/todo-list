from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "tasks/index.html"


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"


def toggle_task(request: HttpRequest, pk: int):
    task = Task.objects.get(pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("tasks:task_list")

