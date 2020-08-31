from django.urls import path
from . import views

urlpatterns = [

    path('', views.causes, name='causes'),

    path('cause-single', views.cause_single, name='cause-single'),

    path('donate', views.donate, name='donate'),

    path('events', views.events, name='events'),

    path('event-single', views.event_single, name='event-single'),


]