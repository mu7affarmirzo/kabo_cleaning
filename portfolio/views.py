from django.shortcuts import render, get_object_or_404
from .models import *


def portfoliosView(request):
    context = {}
    portfolio = PortfolioModel.objects.all()
    context['portfolio'] = portfolio
    return render(request, 'pages/portfolio.html', context)


def individualPortfoliosView(request, slug):
    context = {}
    portfolio = PortfolioModel.objects.get(id=slug)
    blocks = portfolio.blocks.all()
    context['blocks'] = blocks
    return render(request, 'pages/portfolio_individual.html', context)

