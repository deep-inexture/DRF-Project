from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
import json

from products.models import Product
from django.forms.models import model_to_dict


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(data, fields=['id', 'title'])
        """
        model instance (model_data) turn a python dict to return Json to client
        """
    return JsonResponse(data)
