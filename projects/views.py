from django.shortcuts import render, get_object_or_404
from .models import *


def projectsView(request):
    context = {}
    projects = ProjectModel.objects.all()
    context['projects'] = projects
    return render(request, 'pages/projects.html', context)


def individualProjectsView(request, slug):
    context = {}
    # projects = ProjectModel.objects.all()
    # project = get_object_or_404(ProjectModel, id=slug)
    project = ProjectModel.objects.get(id=slug)
    blocks = project.blocks.all()
    context['blocks'] = blocks
    return render(request, 'pages/projects_individual.html', context)

