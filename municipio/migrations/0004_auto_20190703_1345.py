# Generated by Django 2.2.3 on 2019-07-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('municipio', '0003_auto_20190703_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='codigo_m',
            field=models.IntegerField(verbose_name=True),
        ),
    ]
