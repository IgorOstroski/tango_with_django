# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='comments',
            field=models.CharField(default=datetime.date(2018, 12, 11), max_length=600),
            preserve_default=False,
        ),
    ]
