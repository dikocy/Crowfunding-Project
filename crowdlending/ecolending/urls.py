# cette page regroupe tous les urls de mon application ecolending
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('preteurs/', views.preteurs, name='preteurs')
]
