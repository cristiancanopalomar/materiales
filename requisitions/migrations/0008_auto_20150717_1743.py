# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0007_agree'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agree',
            options={'verbose_name': 'accept request', 'verbose_name_plural': 'accept request'},
        ),
        migrations.AddField(
            model_name='agree',
            name='created_agree',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 17, 17, 42, 54, 806344, tzinfo=utc), auto_now_add=True, help_text=b'item creation date', verbose_name='creation date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agree',
            name='description',
            field=models.TextField(default=datetime.datetime(2015, 7, 17, 17, 43, 4, 835052, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='agree',
            unique_together=set([('request',)]),
        ),
    ]
