# Generated by Django 4.2 on 2023-04-26 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]