from django.shortcuts import render
from rest_framework import permissions, generics
from .permissions import IsOwner
from .serializers import RestaurantSerializer, CategorySerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Restaurant, Category

# Create your views here.


class RestaurantList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Restaurant.objects.filter()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RestaurantDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class CategoryList(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
