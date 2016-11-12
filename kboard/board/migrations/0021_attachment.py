# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-10 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0020_auto_20161110_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Post')),
            ],
        ),
    ]