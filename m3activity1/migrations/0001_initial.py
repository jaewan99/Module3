# Generated by Django 5.0.2 on 2024-03-05 00:09

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_name", models.CharField(max_length=100)),
                ("item_price", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            managers=[
                ("object", django.db.models.manager.Manager()),
            ],
        ),
    ]
