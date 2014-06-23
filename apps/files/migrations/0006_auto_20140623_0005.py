# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_file_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created_on',
            field=models.DateField(auto_now=True),
        ),
    ]
