# Project Management System (Promage)

Django REST project management backend (“Promage”) with authentication, projects, tasks, templates, resources, and time logging.

## Stack

- Django + Django REST Framework
- JWT / custom auth under `authentication`
- SQLite DB checked in for local prototyping (`db.sqlite3`)

## Layout (`Promage/`)

| App / package | Role |
|---------------|------|
| `Promage/` | Django project settings |
| `authentication/` | Custom users / auth API |
| `users/` | User-related endpoints |
| `projects/` | Projects (name, manager, due date, status, progress) |
| `tasks/` / `taskmanager/` | Task management |
| `project_templates/` | Reusable project templates |
| `resource_mgmt/` | Resources |
| `timelog/` | Time tracking |
| `dashboard/` / `settings/` | Supporting modules |

## Getting started

```bash
cd Promage
python -m venv .venv
source .venv/bin/activate
pip install django djangorestframework djangorestframework-simplejwt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Explore the admin site and REST endpoints defined in each app’s `urls.py`.

## Notes

- Remove or gitignore local DB files before sharing production data.
- Configure CORS and secrets before deploying.
