# Generated by Django 3.1 on 2020-08-22 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0001_initial'),
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='garage',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='garage.garage'),
        ),
    ]