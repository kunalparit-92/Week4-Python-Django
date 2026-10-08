from django.contrib import admin
from django.urls import path
from tasks.views import task_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', task_api),
]