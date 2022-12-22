# Generated by Django 4.1.4 on 2022-12-22 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jks_site', '0003_alter_choices_footer_alter_content_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='influencer', to='jks_site.influencerspage'),
        ),
        migrations.AlterField(
            model_name='influencermembers',
            name='influencer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='influencer_member', to='jks_site.influencer', verbose_name='Отношение к дому'),
        ),
        migrations.AlterField(
            model_name='influencermembers',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, verbose_name='Статистика инстаграм'),
        ),
        migrations.AlterField(
            model_name='influencermembers',
            name='instagram_statistics',
            field=models.CharField(blank=True, default='В instagram', max_length=100, verbose_name='Заголовок статистика инстаграм'),
        ),
        migrations.AlterField(
            model_name='influencermembers',
            name='tiktok',
            field=models.CharField(blank=True, max_length=100, verbose_name='Статистика tiktok'),
        ),
        migrations.AlterField(
            model_name='influencermembers',
            name='tiktok_statistics',
            field=models.CharField(blank=True, default='В tiktok', max_length=100, verbose_name='Заголовок статистика tiktok'),
        ),
        migrations.AlterField(
            model_name='influencermembers',
            name='youtube',
            field=models.CharField(blank=True, max_length=100, verbose_name='Статистика youtube'),
        ),
        migrations.AlterField(
            model_name='influencermembers',
            name='youtube_statistics',
            field=models.CharField(blank=True, default='В youtube', max_length=100, verbose_name='Заголовок статистика youtube'),
        ),
        migrations.AlterField(
            model_name='influncerphoto',
            name='influencer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='influencer_photo', to='jks_site.influencer', verbose_name='Отношение к инфлюенсеру'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_page_projects', to='jks_site.projectspage'),
        ),
    ]
