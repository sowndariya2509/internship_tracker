from django.urls import path
from . import views

urlpatterns = [
    path('', views.listdata, name='listdata'),
    path('add/', views.add, name='add'),
    path('addsave/', views.addsave, name='addsave'),
    path('edit/<str:regno>/', views.edit, name='edit'),
    path('delete/<str:regno>/', views.delete, name='delete'),
]














