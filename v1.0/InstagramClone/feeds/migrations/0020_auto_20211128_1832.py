# Generated by Django 2.1 on 2021-11-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0019_auto_20211128_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='uploadTimeF',
            field=models.CharField(max_length=60),
        ),
    ]
