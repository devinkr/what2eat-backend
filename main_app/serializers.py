from dataclasses import fields
from rest_framework import serializers
from .models import Restaurant, Category


class RestaurantSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Restaurant
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Category
        fields = "__all__"
