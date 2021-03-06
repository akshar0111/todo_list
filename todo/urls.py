"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from todo_app import views
from frontend import views as front_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='overview'),
    path('item-list/', views.item_list, name = 'item-list'),
    path('item-detial/<str:pk>',views.item_detail, name='item-detial'),
    path('item-create/',views.item_create),
    path('item-update/<str:pk>',views.item_update, name='item-update'),
    path('item-delete/<str:pk>',views.item_delete, name='item-delete'),
    path('list/',front_views.list),
    ]
