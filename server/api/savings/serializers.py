from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Savings



class SavingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Savings
        fields = '__all__'

    def create(self, validated_data):
        return Savings.objects.create(**validated_data)
