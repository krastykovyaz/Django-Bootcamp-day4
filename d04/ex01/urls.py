from django.urls import path
from . import views

urlpatterns = [
    path('django/', views.framework_web, name='django'),
    path('display/', views.show_static_page, name='style'),
    path('templates/', views.template_engine, name='templates')
]