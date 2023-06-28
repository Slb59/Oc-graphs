from django.urls import path
from .views import ProjectListView, ProjectDetailView
from .views import ProjectUpdateView, ProjectCreateView, ProjectDeleteView

app_name = 'graphs'

urlpatterns = [
    path('', ProjectListView.as_view(), name='all'),
    path('projects/<int:pk>/detail',
         ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create/',
         ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/',
         ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/',
         ProjectDeleteView.as_view(), name='project_delete'),
]
