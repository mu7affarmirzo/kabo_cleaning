from django.shortcuts import render

from .models import *


def aboutUs(request):
    context = {}
    promo = PageTitleModel.objects.all()[:1]
    statistics = StatisticsModel.objects.all()[:4]
    missions = MissionModel.objects.all()
    context['promo'] = promo
    context['statistics'] = statistics
    context['missions'] = missions

    return render(request, 'pages/about.html', context)

