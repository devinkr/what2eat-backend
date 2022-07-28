# Generated by Django 4.0.6 on 2022-07-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_restaurant_category_category_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.ManyToManyField(to='main_app.category'),
        ),
    ]