from rest_framework import serializers
from .models import User, Profile, Role


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'mobile_number', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ProfileSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'bio', 'role')
