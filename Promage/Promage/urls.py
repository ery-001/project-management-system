"""
URL configuration for Promage.

Canonical project/task API lives under taskmanager (includes WebSocket-backed updates).
Legacy `projects` / `tasks` apps remain installed for migrations but are not mounted.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Projects + tasks (ViewSets) + real-time status helpers
    path("api/", include("taskmanager.urls")),
    path("api/auth/", include("authentication.urls")),
    path("api/dashboard/", include("dashboard.urls")),
    path("api/timelog/", include("timelog.urls")),
    path("api/resource-mgmt/", include("resource_mgmt.urls")),
    path("api/users/", include("users.urls")),
    path("api/templates/", include("project_templates.urls")),
    path("api/app-settings/", include("app_settings.urls")),
]
