# Generated by Django 5.0.2 on 2024-04-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("m3activity1", "0011_alter_itemorder_item_id_alter_itemorder_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemorder",
            name="quantity",
            field=models.BigIntegerField(),
        ),
    ]
