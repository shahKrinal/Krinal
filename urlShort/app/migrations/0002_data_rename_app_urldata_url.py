# Generated by Django 4.1.6 on 2023-02-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Data",
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
                ("name", models.CharField(max_length=12)),
            ],
        ),
        migrations.RenameField(
            model_name="urldata",
            old_name="app",
            new_name="url",
        ),
    ]