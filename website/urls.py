from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about', views.about, name='about'),

    path('volunteers', views.volunteers, name='volunteers'),

    path('faq', views.faq, name='faq'),

    path('donate', views.donate, name='donate'),

    path('causes', views.causes, name='causes'),

    path('cause-single', views.cause_single, name='cause-single'),

    path('events', views.events, name='events'),

    path('event-single', views.event_single, name='event-single'),

    path('blog', views.blog, name='blog'),

    path('blog-single', views.blog_single, name='blog-single'),

    path('contact', views.contact, name='contact'),

]