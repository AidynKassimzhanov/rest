"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, re_path, include
from user import views
from user.views import WomenAPIDestroy, WomenAPIList, WomenAPIUpdate #, WomenViewSet
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet, basename='women')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    # path('api/v1/', include(router.urls)),
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
    path('', views.index, name='home'),
    path('vue', views.user_app, name='user_app'),
]
