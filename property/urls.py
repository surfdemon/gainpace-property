"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from property.views import PropertyList
from . import views

urlpatterns = [
    path('new/', views.PropertyWizard.as_view(), name='new_property'),
    path('<slug:slug>/', views.property_detail, name='property_detail'),
    path('<slug:slug>/edit/', views.EditProperty.as_view(), name='edit_property'),
    path('<slug:slug>/add_image/)', views.AddImage.as_view(), name='add_image'),
    path('', PropertyList.as_view(), name='property_list'),
]
