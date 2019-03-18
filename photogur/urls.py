"""photogur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import picture_show, pics, picture_search, login_view, logout_view, signup, new_picture, edit_picture, delete_picture, delete_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pictures/<int:id>', picture_show, name='picture_details'),
    path('pictures/<int:id>/edit', edit_picture, name='edit_picture'),
    path('pictures/<int:id>/delete', delete_picture, name='delete_picture'),
    path('pictures/<int:id>/deletecomment', delete_comment, name='delete_comment'),
    path('pictures/', pics, name='picture_home'),
    path('search/', picture_search, name='picture_search'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('newpicture/', new_picture, name='new_picture'),
]
