from django.urls import path
from . import views

app_name = 'logs'

urlpatterns = [
    path('', views.all_logs, name="all_logs"),
    path('<str:day>', views.day_logs, name="day_logs"),
]