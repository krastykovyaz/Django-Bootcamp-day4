from django.urls import path
from . import views

urlpatterns = [
    path('', views.gen_colors, name='table_col')
]