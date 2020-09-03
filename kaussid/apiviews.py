from rest_framework import generics, viewsets

from rest_framework.views import APIView

from . import models, serializers

class Personal_nameViewSet(viewsets.ModelViewSet):
    queryset = models.Personal_name.objects.all()
    serializer_class = serializers.Personal_nameSerializer

class Donate(generics.ListCreateAPIView):
    queryset = models.Donate.objects.all()
    serializer_class = serializers.DonateSerializer

class Organizer(generics.ListCreateAPIView):
    queryset = models.Organizer.objects.all()
    serializer_class = serializers.OrganizerSerializer

class MontantViewSet(viewsets.ModelViewSet):
    queryset = models.Montant.objects.all()
    serializer_class = serializers.MontantSerializer

class Type_don(generics.ListCreateAPIView):
    queryset = models.Type_don.objects.all()
    serializer_class = serializers.Type_donSerializer

class Cause(generics.ListCreateAPIView):
    queryset = models.Cause.objects.all()
    serializer_class = serializers.CauseSerializer

class Event(generics.ListCreateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer