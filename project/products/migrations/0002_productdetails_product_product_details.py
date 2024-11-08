# Generated by Django 5.1.3 on 2024-11-08 19:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductDetails",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("rating", models.IntegerField()),
                ("warranty", models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="product_details",
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="products.productdetails"
            ),
        ),
    ]
