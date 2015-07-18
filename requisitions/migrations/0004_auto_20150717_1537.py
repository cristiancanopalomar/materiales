# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0003_auto_20150717_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='created_requisition',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisition',
            name='description',
            field=models.TextField(help_text=b'description of the requisition'),
            preserve_default=True,
        ),
    ]
