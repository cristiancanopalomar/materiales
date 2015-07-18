# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0008_auto_20150714_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='description',
            field=models.CharField(help_text=b'description of the Component', max_length=100),
            preserve_default=True,
        ),
    ]
