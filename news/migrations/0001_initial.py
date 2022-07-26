# Generated by Django 4.0.6 on 2022-07-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название')),
                ('anons', models.CharField(max_length=201, verbose_name='Анонс')),
                ('content', models.TextField(verbose_name='Контент')),
                ('date', models.DateTimeField(verbose_name='Cоздан')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
