# Generated by Django 5.1 on 2024-09-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='descriere',
            field=models.TextField(),
        ),
    ]
