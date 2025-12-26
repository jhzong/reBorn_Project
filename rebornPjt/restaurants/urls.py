from django.urls import path, include
from . import views

app_name = 'restaurants'
urlpatterns = [
    path('rlist/', views.rlist, name='rlist'),
]
