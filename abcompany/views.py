from django.shortcuts import render

from .models import *


def title(request):
    context = {}
    video = PageTitleModel.objects.all()
    context['video'] = video

    return render(request, 'pages/about.html', context)

