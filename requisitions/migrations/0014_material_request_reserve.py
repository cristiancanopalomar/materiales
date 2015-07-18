# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0013_auto_20150718_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='request_reserve',
            field=models.ForeignKey(default=datetime.datetime(2015, 7, 18, 20, 39, 13, 888319, tzinfo=utc), to='requisitions.Reserve', help_text=b'request number'),
            preserve_default=False,
        ),
    ]
