# Generated by Django 5.0.2 on 2024-03-16 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("m3activity1", "0006_order"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="order",
            new_name="orders",
        ),
    ]
