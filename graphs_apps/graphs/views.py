from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models_project import Project
# from .models_task import Task


class ProjectBaseView(View):
    model = Project
    fields = '__all__'
    sucess_url = reverse_lazy('graphs:all')


class ProjectListView(ProjectBaseView, ListView):
    ...


class ProjectDetailView(ProjectBaseView, DetailView):
    # records = Task.objects.filter(subject=).values_list(*fields)
    ...


class ProjectCreateView(ProjectBaseView, CreateView):
    ...


class ProjectUpdateView(ProjectBaseView, UpdateView):
    ...


class ProjectDeleteView(ProjectBaseView, DeleteView):
    ...
