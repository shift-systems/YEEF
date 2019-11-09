from rest_framework import serializers
from .models import User, Profile, Role
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'mobile_number', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class RoleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


class ProfileSerialiser(serializers.ModelSerializer):
    user = RegistrationSerializer(read_only=True)
    role = RoleSerialiser(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'role', 'avatar')

    def update(self, user_data, validated_data):

        password = user_data.pop('password', None)
        user_id = user_data.get('id')
        user = User.objects.get(id=user_id)
        profile_intance = Profile.objects.get(user=user)

        for key, value in user_data.items():
            if key in ('id', 'email', 'mobile_number'):
                continue
            setattr(user, key, value)

        for (key, value) in validated_data.items():
            if key in ('role', 'avator'):
                continue
            setattr(profile_intance, key, value)
        if password is not None:
            user.set_password(password)
        user.save()
        profile_intance.save()
        return profile_intance


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.')
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.')
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if user.is_superuser:
            user.is_verified = True
            user.save()

        return {
            'email': user.email,
            'mobile_number': user.mobile_number,
            'token': user.token

        }
