# Generated by Django 4.1.6 on 2023-02-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_filedata_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedata',
            name='file',
            field=models.CharField(max_length=200, null=True),
        ),
    ]