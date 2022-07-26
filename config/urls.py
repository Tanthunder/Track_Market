
from django.contrib import admin
from django.urls import path
from config import views

urlpatterns = [
    
    path('monthly_details/', views.monthly_details,name='monthly_details'),
    path('yearly_details/', views.yearly_details,name='yearly_details'),
    path('details/<int:pk>',views.Details.as_view(),name='details'),
    path('', views.home,name='home'),
]
