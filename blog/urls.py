from django.urls import path
from . import views, apiviews

urlpatterns = [
    path('', views.blog, name='blog'),

    path('volunteers', views.volunteers, name='volunteers'),

    path('faq', views.faq, name='faq'),

    path('blog-single', views.blog_single, name='blog-single'),

# Routes des API

    path('faqs', apiviews.Faq.as_view(), name='faqs'),

    path('Volunteers', apiviews.Volunteers.as_view(), name='Volunteers'),

    path('Beneficiaire', apiviews.Beneficiaire.as_view(), name='Beneficiaire'),

    path('Categorie', apiviews.Categorie.as_view(), name='Categorie'),



]