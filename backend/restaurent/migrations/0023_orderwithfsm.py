# Generated by Django 5.0.3 on 2024-10-05 08:20

import django.db.models.deletion
import django_fsm
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurent', '0022_contact'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderWithFSM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.PositiveBigIntegerField(blank=True, null=True)),
                ('delivery_address', models.TextField()),
                ('status', django_fsm.FSMField(choices=[('booked', 'booked'), ('in_process', 'in_process'), ('delivered', 'delivered')], default='booked', max_length=50)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderwithfsm_created_by', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderwithfsm_customer', to=settings.AUTH_USER_MODEL)),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurantwithfsm_order', to='restaurent.restaurant')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderwithfsm_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
