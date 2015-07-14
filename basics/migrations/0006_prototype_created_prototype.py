# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0005_prototype_active_prototype'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototype',
            name='created_prototype',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 20, 12, 25, 825054, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
