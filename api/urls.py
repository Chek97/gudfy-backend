from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('api/tasks/', TaskView.as_view()),
    path('api/task/<pk>', TaskView.as_view(http_method_names=['put']))
]