# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0007_auto_20150713_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sap',
            fields=[
                ('code_sap', models.CharField(max_length=10, unique=True, serialize=False, primary_key=True)),
                ('description', models.CharField(help_text=b'', max_length=25)),
                ('type_sap', models.CharField(max_length=2, choices=[(b'MV', b'sap movement'), (b'DT', b'sap destination'), (b'DV', b'division'), (b'CT', b'storehouse center'), (b'AM', b'storehouse')])),
                ('created_sap', models.DateTimeField(help_text=b'item creation date', verbose_name='creation date', auto_now_add=True)),
                ('active_sap', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'sap records',
                'verbose_name_plural': 'sap records',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='sap',
            unique_together=set([('code_sap', 'description')]),
        ),
    ]
