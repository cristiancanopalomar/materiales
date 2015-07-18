# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import basics.rename


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0004_auto_20150717_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisition',
            name='request',
            field=models.CharField(default=basics.rename.random(), max_length=20, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
