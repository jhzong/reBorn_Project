from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('mlist/', views.mlist, name='mlist'),
]
