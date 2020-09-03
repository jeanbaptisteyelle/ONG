from rest_framework import generics, viewsets

from rest_framework.views import APIView

from . import models, serializers

class Faq(generics.ListCreateAPIView):
    queryset = models.Faq.objects.all()
    serializer_class = serializers.FaqSerializer

class Volunteers(generics.ListCreateAPIView):
    queryset = models.Volunteers.objects.all()
    serializer_class = serializers.VolunteersSerializer

class Beneficiaire(generics.ListCreateAPIView):
    queryset = models.Beneficiaire.objects.all()
    serializer_class = serializers.BeneficiaireSerializer

class Tag(generics.ListCreateAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

class Categorie(generics.ListCreateAPIView):
    queryset = models.Categorie.objects.all()
    serializer_class = serializers.CategorieSerializer


