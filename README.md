# Promage

Django REST project-management API with JWT auth, roles, time logs, resources, and real-time task updates over Channels.

## Layout

```
Promage/
  Promage/              # project config (settings, urls, asgi)
  authentication/       # CustomUser + auth endpoints
  taskmanager/          # canonical Project + Task models (WebSocket updates)
  projects/ / tasks/    # legacy apps kept for migrations — not mounted
  dashboard/
  timelog/
  resource_mgmt/
  users/
  project_templates/
  app_settings/         # key/value app configuration
  manage.py
```

## API (canonical)

- `api/` — projects & tasks (taskmanager)
- `api/auth/`
- `api/dashboard/`
- `api/timelog/`
- `api/resource-mgmt/`
- `api/users/`
- `api/templates/`
- `api/app-settings/`
- WebSocket: `ws/tasks/`

## Run

```bash
cd Promage
python -m venv .venv && source .venv/bin/activate
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers channels
python manage.py migrate
python manage.py runserver
```
