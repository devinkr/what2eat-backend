from django.shortcuts import render
from rest_framework import permissions, generics
from .permissions import IsOwner
from .serializers import RestaurantSerializer, CategorySerializer
from django.contrib.auth.mixins import LoginRequiredMixin
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
