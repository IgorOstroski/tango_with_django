# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20181206_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='title',
            new_name='name',
        ),
    ]
