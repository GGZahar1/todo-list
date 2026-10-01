from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from tasks.models import Task


class IndexView(ListView):
    model = Task
    template_name = "tasks/index.html"

