# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0009_auto_20150717_1455'),
        ('requisitions', '0015_auto_20150718_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='center',
            field=models.ForeignKey(related_name='storehouse center', to='basics.Sap', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='material',
            name='warehouse',
            field=models.ForeignKey(related_name='storehouse', to='basics.Sap', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserve',
            name='reserve',
            field=models.CharField(unique=True, max_length=10),
            preserve_default=True,
        ),
    ]
