# Generated by Django 4.1.4 on 2022-12-22 06:51

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('jks_site', '0002_remove_game_preview_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='footer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='footer_choices', to='jks_site.footer'),
        ),
        migrations.AlterField(
            model_name='content',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='page_content', to='jks_site.videoproductionpage'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_page_partners', to='jks_site.mainpage'),
        ),
        migrations.AlterField(
            model_name='project',
            name='main_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_page_projects', to='jks_site.mainpage'),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('photo', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='about_us/', verbose_name='Фото человека')),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='about_us_people', to='jks_site.aboutuspage')),
            ],
        ),
    ]