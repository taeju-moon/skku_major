"""community_project URL Configuration

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
from snsapp import views
from accounts import views as accounts_views
from scoreapp import views as scoreapp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('postcreate', views.postcreate, name="postcreate"),
    path('detail/<int:post_id>', views.detail, name="detail"),
    path("create_comment/<int:post_id>",
         views.create_comment, name="create_comment"),

    path("login", accounts_views.login, name="login"),
    path("logout", accounts_views.logout, name="logout"),
    path("register", accounts_views.register, name="register"),
    path("mypage", accounts_views.mypage, name="mypage"),
    path("editmypage", accounts_views.editmypage, name="editmypage"),
    path("add_lecture",
         accounts_views.add_lecture, name="add_lecture"),
    path("edit_lecture/<int:lecture_id>",
         accounts_views.edit_lecture, name="edit_lecture"),
    path("delete_lecture/<int:lecture_id>",
         accounts_views.delete_lecture, name="delete_lecture"),
    path("apply_score", accounts_views.apply_score, name="apply_score"),

    path("score", scoreapp_views.home, name="score"),
]
