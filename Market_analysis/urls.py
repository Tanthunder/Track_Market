
from django.contrib import admin
from django.urls import path , include
from config import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('config.urls')),
]
