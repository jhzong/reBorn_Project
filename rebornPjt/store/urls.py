from django.urls import path, include
from . import views

app_name = 'store'
urlpatterns = [
    path('slist/', views.slist, name='slist'),
]
