from django.urls import path
from . import views

urlpatterns = [
    path('', views.cat_list, name='cat_list'),
    path('add/', views.cat_add, name='cat_add'),
    path('edit/<int:pk>/', views.cat_edit, name='cat_edit'),
    path('delete/<int:pk>/', views.cat_delete, name='cat_delete'),
]
