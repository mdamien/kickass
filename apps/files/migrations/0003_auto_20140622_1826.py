# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_remove_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
