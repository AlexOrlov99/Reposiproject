# Generated by Django 3.0 on 2022-03-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_homework_on_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='on_deleted',
        ),
        migrations.AddField(
            model_name='homework',
            name='logo',
            field=models.ImageField(default=2010, upload_to=''),
            preserve_default=False,
        ),
    ]