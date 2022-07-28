from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name="restaurants")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
