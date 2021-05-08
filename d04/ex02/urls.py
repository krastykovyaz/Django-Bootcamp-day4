from django.urls import path
from . import views

urlpatterns = [
    path('', views.like_django, name='like_django')
]