from rest_framework import serializers
from . import models

class Personal_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Personal_name
        fields = '__all__'

class DonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Donate
        fields = '__all__'

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organizer
        fields = '__all__'


class MontantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Montant
        fields = '__all__'

class Type_donSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type_don
        fields = '__all__'

class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cause
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'



