from . import serializers, models

from rest_framework import viewsets, generics

from rest_framework.views import APIView

class Adopt(generics.ListCreateAPIView):
    queryset = models.Adopt.objects.all()
    serializer_class = serializers.AdoptSerializer

class PaymentAmount(generics.CreateAPIView):
    serializer_class = serializers.PaymentAmountSerializer

class TemoignageViewSet(viewsets.ModelViewSet):
    queryset = models.Temoignage.objects.all()
    serializer_class = serializers.TemoignageSerializer

class Fundrising(generics.ListCreateAPIView):
    queryset = models.Fundrising.objects.all()
    serializer_class = serializers.FundrisingSerializer

class Need_help(generics.ListCreateAPIView):
    queryset = models.Need_help.objects.all()
    serializer_class = serializers.Need_helpSerializer


class InformationViewSet(viewsets.ModelViewSet):
    queryset = models.Information.objects.all()
    serializer_class = serializers.InformationSerializer

class Lieu_contact(generics.ListCreateAPIView):
    queryset = models.Lieu_contact.objects.all()
    serializer_class = serializers.Lieu_contactSerializer

