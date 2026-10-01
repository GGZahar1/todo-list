from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "tasks/index.html"


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
