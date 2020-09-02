from rest_framework import serializers

from . import models

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'

class Domaine_donSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Domaine_don
        fields = '__all__'

class ObjectifSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Objectif
        fields = '__all__'

