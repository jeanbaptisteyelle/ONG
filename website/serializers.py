from rest_framework import serializers
from . import models


class NewletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Newletter
        fields = '__all__'

class ReseauSociauSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReseauSociau
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Information
        fields = '__all__'

class Need_helpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Need_help
        fields = '__all__'

class FundrisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fundrising
        fields = '__all__'

class PaymentAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentAmount
        fields = '__all__'

class AdoptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Adopt
        fields = '__all__'



        


