from django.urls import path
from . import views

urlpatterns = [
    path('get/<int:pk>/', views.getSoloItem),
    path('get/', views.getTarea),
    path('post/', views.postTarea),
    path('put/<int:pk>/', views.putTarea),
    path('delete/<int:pk>/', views.deleteTarea),
]   
