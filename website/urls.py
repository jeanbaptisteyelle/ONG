from django.urls import path, include
from . import views
from . import apiviews
# API viewsets

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('website', apiviews.TemoignageViewSet, basename='website-api')
router.register('information', apiviews.InformationViewSet, basename='information-api')

urlpatterns = [
    path('', views.index, name='index'),

    path('contact', views.contact, name='contact'),

# les routes des API

    path('adopt', apiviews.Adopt.as_view(), name='adopt'),

    path('paymentAmount', apiviews.PaymentAmount.as_view(), name='paymentAmount'),

    path('fundrising', apiviews.Fundrising.as_view(), name='fundrising'),

    path('need_help', apiviews.Need_help.as_view(), name='need_help'),

    path('lieu_contact', apiviews.Lieu_contact.as_view(), name='lieu_contact'),

    path("api/", include(router.urls)),

# Fin routes API

]
