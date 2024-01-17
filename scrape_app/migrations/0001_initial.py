# Generated by Django 4.2.4 on 2024-01-17 05:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Business",
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
                ("name", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("website", models.URLField()),
                ("phone_number", models.CharField(max_length=20)),
                ("reviews_count", models.IntegerField()),
                ("reviews_average", models.FloatField()),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
        ),
    ]
