from django.test import TestCase
from tasks.models import Task, Tag
import datetime


class TestModels(TestCase):
    def test_task_str(self):
        tag = Tag.objects.create(name="test")
        task = Task.objects.create(
            content="ABCD",
            deadline=datetime.datetime.now(),
            is_completed=False,
        )
        task.tags.add(tag)
        self.assertEqual(
            str(task),
        f"content: {task.content},"
        f" deadline: {task.deadline},"
        f" is_completed: {task.is_completed}"
        )

    def test_tag_str(self):
        tag = Tag.objects.create(name="test")
        self.assertEqual(str(tag), tag.name)
