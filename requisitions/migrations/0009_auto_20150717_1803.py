# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0008_auto_20150717_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agree',
            name='material',
            field=models.ForeignKey(to='requisitions.Material'),
            preserve_default=True,
        ),
    ]
