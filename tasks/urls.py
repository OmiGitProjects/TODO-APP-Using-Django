from django.urls import path
from .import views

urlpatterns = [
        path('', views.indexHome, name="Homepage"),
        path('update/<str:slug>/', views.editTask, name="editTask"),
        path('delete/<str:slug>/', views.deleteTask, name="deleteTask"),
]