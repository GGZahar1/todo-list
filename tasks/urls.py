from django.urls import path
from tasks.views import TaskListView, TagListView


urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),

]

app_name = "tasks"