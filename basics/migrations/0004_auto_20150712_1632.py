# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0003_auto_20150711_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prototype',
            fields=[
                ('code_prototype', models.CharField(max_length=50, unique=True, serialize=False, primary_key=True)),
                ('type_prototype', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=10)),
                ('make', models.CharField(max_length=3)),
                ('seal_series', models.CharField(max_length=2, blank=True)),
                ('code_color', models.PositiveIntegerField(null=True, blank=True)),
                ('format_prototype', models.CharField(help_text=b'other material format (used in gemini)', max_length=10)),
            ],
            options={
                'verbose_name': 'component serialized',
                'verbose_name_plural': 'component serialized',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='prototype',
            unique_together=set([('code_prototype', 'type_prototype', 'format_prototype')]),
        ),
    ]
