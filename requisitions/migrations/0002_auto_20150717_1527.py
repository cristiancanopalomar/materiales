# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'requested material', 'verbose_name_plural': 'requested material'},
        ),
        migrations.AddField(
            model_name='requisition',
            name='conclude',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='material',
            name='request',
            field=models.ForeignKey(help_text=b'request number', to='requisitions.Requisition'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='material',
            unique_together=set([('request', 'code_sap')]),
        ),
    ]
