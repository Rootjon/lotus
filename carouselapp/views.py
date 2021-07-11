from django.shortcuts import render
from. models import Slider, Feature
from django.db.models import Q, query
from django.shortcuts import redirect

# Create your views here.

def slider (request):
    sliders=Slider.objects.all()[:3]
    features=Feature.objects.all()

    context ={
        'sliders': sliders,
        'features':features

    }

    return render(request,'carousel/index.html',context)
