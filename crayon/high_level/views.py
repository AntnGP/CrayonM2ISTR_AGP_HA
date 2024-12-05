# crayon/views.py
from django.views.generic import DetailView
from .models import Ville, Usine, Local, Siege, Objet, Ressource
from .models import QuantiteRessource, Stock, Etape, Produit
from django.http import JsonResponse


# On ne cherche a avoir QUE les informations sur l'usine_api
# ce qui qsignifie ville, machines productions stock ...
# Mais exclue volontairement des elements comme le siege social


# API view va faire le lien avec tous les elements lies
class UsineApiView(DetailView):
    model = Usine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json_extended())


##### DetailsView


class VilleDetailView(DetailView):
    model = Ville

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class UsineDetailView(DetailView):
    model = Usine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class LocalDetailView(DetailView):
    model = Local

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class SiegeDetailView(DetailView):
    model = Siege

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json_extended())


class ObjetDetailView(DetailView):
    model = Objet

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json_extended())


class RessourceDetailView(DetailView):
    model = Ressource

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json_extended())


class QuantiteRessourceDetailView(DetailView):
    model = QuantiteRessource

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json_extended())


class StockDetailView(DetailView):
    model = Stock

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json_extended())


class EtapeDetailView(DetailView):
    model = Etape

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json_extended())


class ProduitDetailView(DetailView):
    model = Produit

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json_extended())
