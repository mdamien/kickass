# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_auto_20140622_1826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('course', 'created_on')},
        ),
        migrations.AddField(
            model_name='file',
            name='url',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
