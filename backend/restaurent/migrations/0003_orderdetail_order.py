# Generated by Django 5.0.3 on 2024-06-09 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurent', '0002_remove_orderdetail_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='restaurent.order'),
        ),
    ]
