
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('index_2/', views.index_2),
]
