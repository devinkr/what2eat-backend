# Generated by Django 4.0.6 on 2022-07-28 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_restaurant_options_alter_restaurant_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='category',
            new_name='categories',
        ),
    ]