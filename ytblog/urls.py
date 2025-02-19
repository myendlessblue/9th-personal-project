"""ytblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

import blog.views as blog
import account.views as account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.home, name='home'),
    path('blog/<int:blog_id>',blog.detail, name='detail'),
    path('blog/new', blog.new, name="new"),
    path('blog/create', blog.create, name="create"),
    path('blog/edit/<int:blog_id>', blog.edit, name="edit"),
    path('blog/update/<int:blog_id>', blog.update, name="update"),
    path('blog/delete/<int:blog_id>', blog.delete, name="delete"),
    path('blog/comment/<int:blog_id>', blog.add_comment_to_post, name= "add_comment_to_post"),
    path('account/login', account.login_view, name = "login"),
    path('account/logout', account.logout_view, name = "logout"),
    path('account/register', account.register_view, name = "register"),

    path('blog/myyoutube/', blog.myyoutube, name="myyoutube"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)