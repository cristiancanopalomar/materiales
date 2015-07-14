# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0006_prototype_created_prototype'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='created_component',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 20, 17, 10, 509240, tzinfo=utc), auto_now_add=True, help_text=b'item creation date', verbose_name='creation date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='created_process',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 20, 17, 20, 615394, tzinfo=utc), auto_now_add=True, help_text=b'item creation date', verbose_name='creation date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='component',
            name='description',
            field=models.CharField(help_text=b'description of the Component', max_length=100, verbose_name='creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prototype',
            name='created_prototype',
            field=models.DateTimeField(help_text=b'item creation date', verbose_name='creation date', auto_now_add=True),
            preserve_default=True,
        ),
    ]
