# Generated by Django 2.1.15 on 2021-12-12 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0028_auto_20211211_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='pictureF',
            field=models.FileField(default='settings.MEDIA_ROOT/apple.jpg', upload_to='media/'),
        ),
    ]
