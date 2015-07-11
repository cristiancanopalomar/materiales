# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import basics.rename


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0002_auto_20150711_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('code_component', models.PositiveIntegerField(unique=True)),
                ('code_sap', models.CharField(help_text=b'material code (trading system SAP)', max_length=10, unique=True, serialize=False, primary_key=True)),
                ('description', models.CharField(help_text=b'description of the Component', max_length=100)),
                ('image', models.ImageField(upload_to=basics.rename.rename_file(b'upload/basic/component'))),
                ('unit', models.CharField(max_length=2, choices=[(b'M', b'meters'), (b'CU', b'units')])),
                ('active_component', models.BooleanField(default=True)),
                ('type_process', models.ForeignKey(to='basics.Process')),
            ],
            options={
                'verbose_name': 'component not serialized',
                'verbose_name_plural': 'component not serialized',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='component',
            unique_together=set([('code_component', 'code_sap', 'description')]),
        ),
        migrations.RenameField(
            model_name='process',
            old_name='active',
            new_name='active_process',
        ),
        migrations.RenameField(
            model_name='process',
            old_name='code',
            new_name='code_process',
        ),
        migrations.AlterUniqueTogether(
            name='process',
            unique_together=set([('code_process', 'type_process')]),
        ),
    ]
