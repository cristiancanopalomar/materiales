# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import basics.rename


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0009_auto_20150717_1455'),
        ('requisitions', '0012_auto_20150717_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('request', models.ForeignKey(primary_key=True, serialize=False, to='requisitions.Requisition', unique=True)),
                ('reserve', models.CharField(max_length=10)),
                ('order', models.CharField(max_length=25, verbose_name='order of budget')),
                ('created_reserve', models.DateTimeField(help_text=b'item creation date', verbose_name='creation date', auto_now_add=True)),
                ('support', models.FileField(upload_to=basics.rename.rename_file(b'upload/requisition/reserve'))),
                ('closing', models.BooleanField(default=False)),
                ('division', models.ForeignKey(related_name='division', to='basics.Sap')),
                ('sap_destination', models.ForeignKey(related_name='sap destination', to='basics.Sap')),
                ('sap_movement', models.ForeignKey(related_name='sap movement', to='basics.Sap')),
            ],
            options={
                'verbose_name': 'reserve',
                'verbose_name_plural': 'reserves',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='reserve',
            unique_together=set([('request', 'reserve')]),
        ),
    ]
