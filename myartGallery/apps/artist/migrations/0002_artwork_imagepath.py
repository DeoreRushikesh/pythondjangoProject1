# Generated by Django 4.2.5 on 2023-10-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='imagePath',
            field=models.CharField(default='', max_length=1000),
        ),
    ]