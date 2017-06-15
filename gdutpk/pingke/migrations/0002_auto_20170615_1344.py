# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-15 13:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pingke', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
           name='Course_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_type',
       ),
        migrations.AlterField(
            model_name='course',
            name='profile',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(default='unknow', to='pingke.Teacher'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='dept',
            name='name_eng',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='major',
            name='code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='major',
            name='name_eng',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='guest',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pingke.GdutGuest'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]