from django.urls import path
from concurrent_api import views

urlpatterns = [
    path('concurrent_api.html', views.home, name='home'),
]