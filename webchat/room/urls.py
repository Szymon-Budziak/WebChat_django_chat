from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('newroom/', views.new_room, name='new_room'),
    path('<slug:slug>/', views.room, name='room'),
]
