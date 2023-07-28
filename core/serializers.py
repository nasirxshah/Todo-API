from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework.settings import api_settings



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username','email','password']

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            print(api_settings.NON_FIELD_ERRORS_KEY)
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error[api_settings.NON_FIELD_ERRORS_KEY]}
            )
        return attrs
    
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    