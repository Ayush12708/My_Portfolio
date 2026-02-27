from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('debug/', views.debug_view, name='debug_view'),
]
