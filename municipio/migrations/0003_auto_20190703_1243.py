# Generated by Django 2.2.3 on 2019-07-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('municipio', '0002_auto_20190703_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='codigo_m',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='codigo_r',
            field=models.IntegerField(unique=True),
        ),
    ]