# Generated by Django 5.0.3 on 2024-06-09 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurent', '0008_delete_delivery'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('customer_name', models.CharField(max_length=200)),
                ('customer_address', models.TextField()),
                ('customer_phone', models.CharField(max_length=15)),
                ('delivery_status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], max_length=50)),
                ('delivery_time', models.DateTimeField()),
                ('delivery_person_name', models.CharField(blank=True, max_length=200, null=True)),
                ('delivery_person_contact', models.CharField(blank=True, max_length=15, null=True)),
                ('restaurant_name', models.CharField(max_length=200)),
                ('restaurant_address', models.TextField()),
                ('restaurant_phone', models.CharField(max_length=15)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='restaurent.order')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
