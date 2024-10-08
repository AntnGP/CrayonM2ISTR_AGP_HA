# election/views.py
from django.views.generic import DetailView
from .models import Ville, Usine, Local
from django.http import JsonResponse


class VilleDetailView(DetailView):
    model = Ville

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class LocalDetailView(DetailView):
    model = Local

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class UsineApiView(DetailView):
    model = Usine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json_extended())


class UsineDetailView(DetailView):
    model = Usine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json_extended())
