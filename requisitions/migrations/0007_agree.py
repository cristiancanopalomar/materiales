# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisitions', '0006_auto_20150717_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agree',
            fields=[
                ('request', models.ForeignKey(primary_key=True, serialize=False, to='requisitions.Requisition', unique=True)),
                ('material', models.ManyToManyField(to='requisitions.Material')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
