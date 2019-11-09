from django.contrib.auth import authenticate
from rest_framework import serializers
from api.authentication.serializers import RegistrationSerializer

from .models import Savings


class SavingsSerializer(serializers.ModelSerializer):
    saver = RegistrationSerializer(read_only=True)

    class Meta:
        model = Savings
        fields = ('id', 'amount', 'transaction_id',
                  'transaction_ref_id', 'status',
                  'financial_transaction_id', 'saver')

    def create(self, validated_data):
        return Savings.objects.create(**validated_data)
