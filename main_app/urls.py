from django.urls import path, include
from main_app import views

urlpatterns = [
    path("restaurants/", views.RestaurantList.as_view(), name="restaurant_list"),
    path(
        "restaurants/<int:pk>/",
        views.RestaurantDetail.as_view(),
        name="restaurant_detail",
    ),
    path("categories/", views.CategoryList.as_view(), name="category_list"),
    path(
        "categories/<int:pk>/", views.CategoryDetail.as_view(), name="category_detail"
    ),
    path("", views.redirect_view),
]
