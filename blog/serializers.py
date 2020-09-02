from rest_framework import serializers

from . import models

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faq
        fields = '__all__'

class VolunteersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Volunteers
        fields = '__all__'

class BeneficiaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Beneficiaire
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categorie
        fields = '__all__'





