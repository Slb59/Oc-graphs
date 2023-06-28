"""
URL configuration for grpahs project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('graphs_apps.graphs.urls', namespace='graphs')),
    path("admin/", admin.site.urls),
]
