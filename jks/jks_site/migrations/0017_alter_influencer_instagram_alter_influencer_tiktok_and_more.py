# Generated by Django 4.1.4 on 2022-12-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jks_site', '0016_seriesfilms_photo_seriesfilms_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, verbose_name='Статистика инстаграм'),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='tiktok',
            field=models.CharField(blank=True, max_length=100, verbose_name='Статистика tiktok'),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='youtube',
            field=models.CharField(blank=True, max_length=100, verbose_name='Статистика youtube'),
        ),
    ]
