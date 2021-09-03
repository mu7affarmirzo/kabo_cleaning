from django.shortcuts import render

from .models import *


def aboutUs(request):
    context = {}
    promo = PageTitleModel.objects.all()[:1]
    statistics = StatisticsModel.objects.all()[:4]
    missions = MissionModel.objects.all()
    company_missions = CompanyMissionModel.objects.all()[:1]
    team = TeamModel.objects.all()[:6]
    context['promo'] = promo
    context['statistics'] = statistics
    context['missions'] = missions
    context['company_missions'] = company_missions
    context['team'] = team

    return render(request, 'pages/about.html', context)

