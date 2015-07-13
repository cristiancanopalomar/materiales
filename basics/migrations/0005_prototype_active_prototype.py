# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0004_auto_20150712_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototype',
            name='active_prototype',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
