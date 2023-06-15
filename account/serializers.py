from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError

from .models import CustomUser


def validate_password_characters(value):
    if not any(char.isalpha() and char.isupper() for char in value):
        raise ValidationError(
            "Пароль должен содержать как минимум одну заглавную букву.",
            code='password_no_uppercase'
        )
    if not any(char.isalpha() and not char.isupper() for char in value):
        raise ValidationError(
            "Пароль должен содержать как минимум одну строчную букву.",
            code='password_no_lowercase'
        )
    if len(value) < 8:
        raise serializers.ValidationError("Password must be at least 8 characters long.",
                                          code='password-length-lower-8')
    if len(value) > 15:
        raise serializers.ValidationError("Password must not exceed 15 characters.",
                                          code='password-length-higher-15')

    if not any(char.isdigit() for char in value):
        raise serializers.ValidationError("Password must contain at least one digit.")

    if not any(char.isalnum() for char in value):
        raise serializers.ValidationError("Password must contain at least one special character.")





class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password_characters])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'password')


class RegisterUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('photo', 'first_name', 'last_name', 'patronymic', 'date_of_birth', 'phone_number', 'email')

    def update(self, instance, validated_date):
        instance.photo = validated_date.get('photo', instance.photo)
        instance.first_name = validated_date.get('first_name', instance.first_name)
        instance.last_name = validated_date.get('last_name', instance.last_name)
        instance.patronymic = validated_date.get('patronymic', instance.patronymic)
        instance.date_of_birth = validated_date.get('date_of_birth', instance.date_of_birth)
        instance.phone_number = validated_date.get('phone_number', instance.phone_number)
        instance.email = validated_date.get('email', instance.email)

        instance.save()

        return instance

