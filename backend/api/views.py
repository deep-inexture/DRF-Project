from django.shortcuts import render

from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    print(request.GET)
    print(request.POST)
    body = request.body                     # byte string of Json data
    data = {}
    try:
        data = json.loads(body)             # String of Json data -> Python Dictionary
    except:
        pass
    print(data.keys())
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)   # request.Meta
    data['content_type'] = request.content_type
    return JsonResponse(data)
