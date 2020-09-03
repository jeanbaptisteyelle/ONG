from django.urls import path
from . import views
from . import apiviews

urlpatterns = [
    path('', views.about, name='about'),

# Routes des API

    path('objectif', apiviews.Objectif.as_view(), name='objectif'),

    path('domaine_don', apiviews.Domaine_don.as_view(), name='domaine_don'),

    path('service', apiviews.Service.as_view(), name='service'),

    path('aboutlist', apiviews.About.as_view(), name='aboutlist'),

# Fin Routes des API
]