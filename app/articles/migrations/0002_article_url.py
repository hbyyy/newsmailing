# Generated by Django 3.0.7 on 2020-06-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.URLField(blank=True, verbose_name='article url'),
        ),
    ]