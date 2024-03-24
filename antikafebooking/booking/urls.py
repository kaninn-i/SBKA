from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dates/<int:date_id>/', views.dates),  # id поменять на саму дату
]
