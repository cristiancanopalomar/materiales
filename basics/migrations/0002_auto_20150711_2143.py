# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
