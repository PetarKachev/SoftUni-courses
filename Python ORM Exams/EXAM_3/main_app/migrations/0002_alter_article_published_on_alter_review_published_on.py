# Generated by Django 5.0.6 on 2024-07-21 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='published_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
