from django.urls import path
from tasks.views import TaskListView, TagListView, toggle_task

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("task/<int:pk>/toggle/", toggle_task, name="toggle_task")

]

app_name = "tasks"