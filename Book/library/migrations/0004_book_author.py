# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_bookname'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='unknown', max_length=200),
            preserve_default=False,
        ),
    ]
