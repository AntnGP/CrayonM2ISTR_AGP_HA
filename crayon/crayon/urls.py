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
    ##ApiView
    path(
        "usine_api/<int:pk>",
        views.UsineApiView.as_view(),
        name="usine_api",
    ),
    ##DetailView
    path(
        "ville/<int:pk>",
        views.VilleDetailView.as_view(),
        name="ville",
    ),
    path(
        "usine/<int:pk>",
        views.UsineDetailView.as_view(),
        name="usine",
    ),
    path(
        "local/<int:pk>",
        views.LocalDetailView.as_view(),
        name="local",
    ),
    path(
        "siege/<int:pk>",
        views.SiegeDetailView.as_view(),
        name="siege",
    ),
    path(
        "objet/<int:pk>",
        views.Objet.as_view(),
        name="objet",
    ),
    path(
        "ressource/<int:pk>",
        views.RessourceDetailView.as_view(),
        name="ressource",
    ),
    path(
        "qantite_ressource/<int:pk>",
        views.QuantiteRessourceDetailView.as_view(),
        name="quantite_ressource",
    ),
    path(
        "stock/<int:pk>",
        views.StockDetailView.as_view(),
        name="stock",
    ),
    path(
        "etape/<int:pk>",
        views.EtapeDetailView.as_view(),
        name="etape",
    ),
    path(
        "produit/<int:pk>",
        views.ProduitDetailView.as_view(),
        name="produit",
    ),
]
