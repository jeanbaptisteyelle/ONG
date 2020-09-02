from django.urls import path
from . import views
from . import apiviews

urlpatterns = [
    path('', views.index, name='index'),

    path('contact', views.contact, name='contact'),

]