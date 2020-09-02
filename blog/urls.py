from django.urls import path
from . import views
from . import apiviews

urlpatterns = [
    path('', views.blog, name='blog'),

    path('volunteers', views.volunteers, name='volunteers'),

    path('faq', views.faq, name='faq'),

    path('blog-single', views.blog_single, name='blog-single'),

]