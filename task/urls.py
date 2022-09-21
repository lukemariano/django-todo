from django.urls import path

from .views import *

urlpatterns = [
    path('', TaskView.as_view(), name="task.list")
]
