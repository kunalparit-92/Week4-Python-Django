from django.contrib import admin
from django.urls import path
from tasks.views import get_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', get_tasks),
]