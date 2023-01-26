"""Conference_Room_Reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Reservation_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Base, name='base'),
    path('home_page/', views.HomePage, name='home'),
    path('room/new/', views.AddRoom, name='adding'),
    # path('room/<int:id>', views.RoomDetails, name='details'),
    path('room/modify/<int:id>', views.Modify, name='modify'),
    path('room/delete/<int:id>', views.Delete, name='delete'),
    # path('room/reserve/<int:id>', views.Reserve, name='reserve'),
]
