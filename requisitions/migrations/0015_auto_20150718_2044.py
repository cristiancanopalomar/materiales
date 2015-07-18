# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0014_material_request_reserve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='request_reserve',
            field=models.ForeignKey(to='requisitions.Reserve', help_text=b'request number', null=True),
            preserve_default=True,
        ),
    ]
