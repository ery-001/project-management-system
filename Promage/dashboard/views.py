from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count
from projects.models import Project
from timelog.models import TimeLog
from resource_mgmt.models import Resource
from .models import DashboardStats

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stats, created = DashboardStats.objects.get_or_create()
        stats.total_projects = Project.objects.count()
        stats.total_hours = TimeLog.objects.aggregate(Sum("hours_spent"))["hours_spent__sum"] or 0
        stats.total_resources = Resource.objects.count()
        stats.save()

        return Response({"total_projects": stats.total_projects, "total_hours": stats.total_hours, "total_resources": stats.total_resources})
