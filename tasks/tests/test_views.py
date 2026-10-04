import datetime

from django.test import TestCase
from django.urls import reverse

from tasks.models import Task, Tag

TASK_URL = reverse("tasks:task-list")
TAG_URL = reverse("tasks:tag-list")

class TestViews(TestCase):
    def test_status_code(self):
        response_task = self.client.get(TASK_URL)
        self.assertEqual(response_task.status_code, 200)
        response_tag = self.client.get(TAG_URL)
        self.assertEqual(response_tag.status_code, 200)

    def test_template_user(self):
        response_task = self.client.get(TASK_URL)
        self.assertTemplateUsed(response_task, "tasks/index.html")
        response_tag = self.client.get(TAG_URL)
        self.assertTemplateUsed(response_tag, "tasks/tag_list.html")

    def test_retrieve_task(self):
        Task.objects.create(
            content="Test Task",
            deadline=datetime.datetime.now(),
            is_completed=False)
        Task.objects.create(
            content="Test 12",
            deadline=datetime.datetime.now(),
            is_completed=True)
        Task.objects.create(
            content="Test 2",
            deadline=datetime.datetime.now(),
            is_completed=True)
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(list(response.context["task_list"]), list(tasks))

    def test_retrieve_tag(self):
        Tag.objects.create(
            name="Test Tag",
        )
        Tag.objects.create(
            name="Test Tag2",
        )
        response = self.client.get(TAG_URL)
        self.assertEqual(response.status_code, 200)
        tags = Tag.objects.all()
        self.assertEqual(list(response.context["tag_list"]), list(tags))

    def test_complete_task(self):
        task = Task.objects.create(
            content="Test Task",
            deadline=datetime.datetime.now(),
            is_completed=False
        )
        self.client.post(
            reverse("tasks:toggle-task", kwargs={"pk": task.pk}),
        )
        task.refresh_from_db()
        self.assertTrue(task.is_completed)

    def test_undo_task(self):
        task = Task.objects.create(
            content="Test Task",
            is_completed=True,
        )

        self.client.post(
            reverse("tasks:toggle-task", args=[task.pk])
        )

        task.refresh_from_db()

        self.assertFalse(task.is_completed)
