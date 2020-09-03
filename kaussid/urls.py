from django.urls import path, include
from . import views, apiviews

# Routes viewsets

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('kaussid', apiviews.Personal_nameViewSet, basename='api-kaussid')
router.register('montant', apiviews.MontantViewSet, basename='api-montant')


urlpatterns = [

    path('', views.causes, name='causes'),

    path('cause-single', views.cause_single, name='cause-single'),

    path('donate', views.donate, name='donate'),

    path('events', views.events, name='events'),

    path('event-single', views.event_single, name='event-single'),

# Routes des API

    path('donates', apiviews.Donate.as_view(), name='donates'),

    path('Organizer', apiviews.Organizer.as_view(), name='Organizer'),

    path('Type_don', apiviews.Type_don.as_view(), name='Type_don'),

    path('cause', apiviews.Cause.as_view(), name='Cause'),

    path('event', apiviews.Event.as_view(), name='Event'),

    path('api/', include(router.urls)),

# Fin Routes des API
]