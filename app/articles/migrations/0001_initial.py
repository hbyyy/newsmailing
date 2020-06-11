# Generated by Django 3.0.6 on 2020-06-11 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='company name')),
                ('oid', models.CharField(max_length=4, verbose_name='company number')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('subtitle', models.TextField(blank=True, verbose_name='subtitle')),
                ('contents', models.TextField(verbose_name='contents')),
                ('aid', models.CharField(max_length=12, unique=True, verbose_name='article number')),
                ('pub_date', models.DateField(verbose_name='publishing date')),
                ('pub_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='articles.Company', verbose_name='publishing company')),
            ],
        ),
    ]
