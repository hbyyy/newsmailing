# Generated by Django 3.0.6 on 2020-06-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20200611_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='keywords',
            field=models.ManyToManyField(db_table='subscribe', related_name='profiles', to='members.Keyword', verbose_name='keyword'),
        ),
    ]
