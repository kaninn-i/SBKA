from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dates/<slug:date_slug>/', views.date, name='dates'),
    path('bookings/<int:pk>/edit', views.edit_booking),
]
