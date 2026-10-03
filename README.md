# Todo List

A simple Todo List web application built with Django.

## Features

- Create, update and delete tasks
- Mark tasks as completed or undo completion
- Set optional deadlines
- Add multiple tags to tasks
- Create, update and delete tags
- Tasks are ordered by completion status and creation date

## Technologies

- Python
- Django
- SQLite
- Bootstrap 4

## Installation

```bash
git clone <your-repository-url>
cd todo-list-2

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

