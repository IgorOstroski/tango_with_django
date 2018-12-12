# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20181206_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='title',
            new_name='name',
        ),
    ]
