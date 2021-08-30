from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class NewsView(TemplateView):
    template_name = 'news.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class ProjectsView(TemplateView):
    template_name = 'projects.html'


def about_page(request):
    context = {}
    return render(request, 'about.html', context)


def just_page(request):
    context = {}
    return render(request, 'about.html', context)


