from dataclasses import fields
from wsgiref.validate import validator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Restaurant, Category


class RestaurantSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Restaurant
        fields = ["id", "name"]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")
    restaurants = RestaurantSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "title", "restaurants"]


# https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
