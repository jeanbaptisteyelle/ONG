from django.urls import path
from . import views
from . import apiviews

urlpatterns = [
    path('', views.about, name='about'),
]