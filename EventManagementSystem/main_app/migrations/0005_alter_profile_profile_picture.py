# Generated by Django 5.1.3 on 2024-11-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_event_profile_alter_event_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]