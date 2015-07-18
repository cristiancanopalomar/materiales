# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0005_auto_20150717_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='material',
            name='code_sap',
            field=models.ForeignKey(help_text=b'sap basic model code', to='basics.Component'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='material',
            name='dispatched',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
