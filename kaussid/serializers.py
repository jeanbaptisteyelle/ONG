from rest_framework import serializers

from . import models

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Event
        fields = '__all__'


class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Cause
        fields = '__all__'

class Type_donSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Type_don
        fields = '__all__'

class MontantSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Montant
        fields = '__all__'

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Organizer
        fields = '__all__'

class DonateSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Donate
        fields = '__all__'s

class Personal_nameSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Personal_name
        fields = '__all__'


