"""
URL configuration for crayon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from high_level import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "ville/<int:pk>",
        views.VilleDetailView.as_view(),
        name="ville",
    ),
    path(
        "local/<int:pk>",
        views.LocalDetailView.as_view(),
        name="local",
    ),
    path(
        "usine/<int:pk>",
        views.UsineDetailView.as_view(),
        name="usine",
    ),
    path(
        "usine_api/<int:pk>",
        views.UsineApiView.as_view(),
        name="usine_api",
    ),
]
