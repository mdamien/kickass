# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20140622_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='hidden',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
