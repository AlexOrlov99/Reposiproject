# Generated by Django 4.0.2 on 2022-03-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20220211_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='datatime_created',
            field=models.DateTimeField(auto_now=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='account',
            name='datatime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
        migrations.AlterField(
            model_name='group',
            name='datatime_created',
            field=models.DateTimeField(auto_now=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='group',
            name='datatime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='datatime_created',
            field=models.DateTimeField(auto_now=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='datatime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
        migrations.AlterField(
            model_name='student',
            name='datatime_created',
            field=models.DateTimeField(auto_now=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='student',
            name='datatime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
    ]
