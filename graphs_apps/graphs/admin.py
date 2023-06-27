from django.contrib import admin

from .models import Project


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
