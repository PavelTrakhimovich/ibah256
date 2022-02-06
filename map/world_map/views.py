from django.shortcuts import render
from .models import Coordinats
from django.http import JsonResponse


def map_view(request):
    return render(request, 'world_map/map.html')


def list_cliks(request):
    res = Coordinats.objects.all()
    return render(request, 'world_map/list.html', {'res': res})


def save_coordinates(request):
    if request.method == "GET":
        lat = request.GET.get("lat", None)
        lng = request.GET.get("lng", None)
        if lat != None and lng != None:
            res = Coordinats(pointer=(str(lat) +"   "+ str(lng)))
            res.save()
            return JsonResponse({"valid":True}, status = 200)
        else:
            return JsonResponse({"valid":False}, status = 400)