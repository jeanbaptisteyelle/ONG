from rest_framework import generics,viewsets

from rest_framework.views import APIView

from . import serializers, models

class Objectif(generics.ListCreateAPIView):
    queryset = models.Objectif.objects.all()
    serializer_class = serializers.ObjectifSerializer

class Domaine_don(generics.ListCreateAPIView):
    queryset = models.Domaine_don.objects.all()
    serializer_class = serializers.Domaine_donSerializer

class Service(generics.ListCreateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class About(generics.ListCreateAPIView):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer

