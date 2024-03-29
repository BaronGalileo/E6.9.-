"""
URL configuration for messanger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from messanger_chat.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('messanger_chat.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/RoomList/', RoomAPIList.as_view()),
    path('api/v1/RoomList/<int:pk>', RoomDetailView.as_view(), name='room_api'),
    path('api/v1/ProfileList/', ProfileAPIList.as_view()),
    path('api/v1/ProfileList/<int:pk>', ProfileDetailView.as_view(), name='profile_api'),


]
