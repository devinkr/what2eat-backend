# Generated by Django 4.0.6 on 2022-07-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='main_app.category'),
        ),
    ]
