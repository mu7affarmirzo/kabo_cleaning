from .views import *
from django.urls import path

app_name = 'abcompany'

urlpatterns = [
    path('title/', title, name='title'),
    # path('home', HomeView.as_view(), name='home'),
    # path('contacts', ContactsView.as_view(), name='contacts'),
    # path('portfolio', PortfolioView.as_view(), name='portfolio'),
    # path('projects', ProjectsView.as_view(), name='projects'),
    # path('news', NewsView.as_view(), name='news'),
    # path('home', HomeView.as_view(), name='home'),
    # path('home', HomeView.as_view(), name='home'),
    # path('home', HomeView.as_view(), name='home'),
    # path('home', HomeView.as_view(), name='home'),
    # path('page', about_page, name='about-page'),
]
