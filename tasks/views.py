from django.http import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from tasks.forms import TaskForm
from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "tasks/index.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/confirm_delete_task.html"
    success_url = reverse_lazy("tasks:task-list")


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_form.html"


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/comfirm_delete_tag.html"


class ToggleTask(View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponseRedirect:
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect("tasks:task-list")
