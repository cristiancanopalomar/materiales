# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0009_auto_20150717_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agree',
            name='material',
            field=models.ManyToManyField(to='requisitions.Material'),
            preserve_default=True,
        ),
    ]
