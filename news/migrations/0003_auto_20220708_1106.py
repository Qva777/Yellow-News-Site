# Generated by Django 3.2.9 on 2022-07-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articles_anons_alter_articles_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='articles',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='articles',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]