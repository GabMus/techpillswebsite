from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.


def index(request):
    videos = Video.objects.order_by('-date_time') # -field means descending
    videos_l = [
        videos[0],
        videos[1]
    ]
    context = {'videos': videos_l}
    return render(request, 'landing/index.html', context)

def gear(request):
    gear_l = Gear.objects.order_by('id')
    context = {'gearList': gear_l}
    return render(request, 'landing/gear.html', context)
