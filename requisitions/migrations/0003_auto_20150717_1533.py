# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0002_auto_20150717_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='created_requisition',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
