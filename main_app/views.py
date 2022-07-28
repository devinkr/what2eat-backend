from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .permissions import IsOwner
from .serializers import RestaurantSerializer, CategorySerializer, RegisterSerializer
from .models import Restaurant, Category

# Create your views here.


class RestaurantList(generics.ListCreateAPIView):
    permission_classes = [IsOwner]
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        owner = self.request.user
        return Restaurant.objects.filter(owner=owner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class CategoryList(generics.ListCreateAPIView):
    permission_classes = [IsOwner]
    serializer_class = CategorySerializer

    def get_queryset(self):
        owner = self.request.user
        return Category.objects.filter(owner=owner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
