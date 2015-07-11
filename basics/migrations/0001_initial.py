# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.PositiveIntegerField()),
                ('description', models.CharField(help_text=b'description of the material or activity', max_length=15)),
                ('type_process', models.CharField(max_length=1, choices=[(b'M', b'material'), (b'A', b'activity')])),
                ('active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'code [process - activity]',
                'verbose_name_plural': 'code [process - activity]',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='process',
            unique_together=set([('code', 'type_process')]),
        ),
    ]
