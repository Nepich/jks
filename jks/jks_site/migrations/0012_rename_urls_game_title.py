# Generated by Django 4.1.4 on 2022-12-22 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jks_site', '0011_remove_gamedevpage_third_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='urls',
            new_name='title',
        ),
    ]