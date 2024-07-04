# Generated by Django 5.0.3 on 2024-06-09 15:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurent', '0005_promotion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promotion_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='promotion',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_promotions', to='restaurent.restaurant'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promotion_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
