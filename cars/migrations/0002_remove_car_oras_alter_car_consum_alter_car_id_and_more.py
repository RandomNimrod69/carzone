# Generated by Django 5.1 on 2024-09-01 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='oras',
        ),
        migrations.AlterField(
            model_name='car',
            name='consum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='kilometraj',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='pasageri',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='pret',
            field=models.IntegerField(),
        ),
    ]
