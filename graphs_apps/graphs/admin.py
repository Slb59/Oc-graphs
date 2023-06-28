from django.contrib import admin

from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "subject", "title", "description",
        "pct_total_time", "nb_hours_on_project"
        ]
    # list_filter = ["type"]
    search_fields = ["title", "description"]
    # raw_id_fields = ["contributors"]
    ordering = ('estimate_start_date',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "date_task", "subject", "category",
        "estimate_time", "real_time"
        ]
    list_filter = ["category"]
    search_fields = ["subject", "description"]
    raw_id_fields = ["subject"]
    ordering = ('date_task', 'category')
