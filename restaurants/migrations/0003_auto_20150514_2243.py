# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20150514_0745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='website',
            new_name='menus',
        ),
    ]
