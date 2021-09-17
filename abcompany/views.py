from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *


def vacancy(request):
    context = {}
    vacancies = VacancyModel.objects.all()
    context['vacancies'] = vacancies
    return render(request, 'pages/vacancy.html', context)


def vacancy_individual(request, slug):
    context = {}
    vacancy = get_object_or_404(VacancyModel, slug=slug)
    context['vacancy'] = vacancy
    return render(request, 'pages/vacancy-individual.html', context)


def partners(request):
    context = {}
    partners = PartnersModel.objects.all()
    context['partners'] = partners
    return render(request, 'pages/partners.html', context)


def partners_individual(request, slug):
    context = {}
    partner = get_object_or_404(PartnersModel, id=slug)
    context['partner'] = partner
    return render(request, 'pages/partners-individual.html', context)


def downloads(request):
    context = {}
    downloads = DownloadsModel.objects.all()
    context['downloads'] = downloads
    return render(request, 'pages/downloads.html', context)


def aboutUs(request):
    context = {}
    promo = PageTitleModel.objects.all()[:1]
    statistics = StatisticsModel.objects.all()[:4]
    missions = MissionModel.objects.all()
    company_missions = CompanyMissionModel.objects.all()[:1]
    team = TeamModel.objects.all()[:6]
    context = {
        'promo': promo,
        'statistics': statistics,
        'missions': missions,
        'company_missions': company_missions,
        'team': team,
    }
    # context['promo'] = promo
    # context['statistics'] = statistics
    # context['missions'] = missions
    # context['company_missions'] = company_missions
    # context['team'] = team

    return render(request, 'pages/about.html', context)


def send_us_cv_view(request):

    context = {}

    form = SendResumeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)

        obj.save()
        form = SendResumeForm()
        return redirect('home')

    context['form'] = form

    return render(request, "contact-us.html", context)

