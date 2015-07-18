# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0009_auto_20150717_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('solicitude', models.DecimalField(default=0, verbose_name='quantity applied', max_digits=7, decimal_places=2)),
                ('created_solicitude', models.DateTimeField(help_text=b'item creation date', verbose_name='creation date', auto_now_add=True)),
                ('generated', models.DecimalField(default=0, verbose_name='quantity generated', max_digits=7, decimal_places=2)),
                ('created_generated', models.DateTimeField(help_text=b'item creation date', null=True, verbose_name='creation date')),
                ('delivered', models.DecimalField(default=0, verbose_name='quantity delivered', max_digits=7, decimal_places=2)),
                ('created_delivered', models.DateTimeField(help_text=b'item creation date', null=True, verbose_name='creation date')),
                ('approved', models.BooleanField(default=False, help_text=b'action defined by the manager')),
                ('dispatched', models.BooleanField(default=False, help_text=b'dispatched central warehouse')),
                ('code_sap', models.ForeignKey(help_text=b'', to='basics.Component')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('request', models.CharField(max_length=20, unique=True, serialize=False, primary_key=True)),
                ('created_requisition', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(help_text=b'description of the requisition', max_length=100)),
            ],
            options={
                'verbose_name': 'requisition',
                'verbose_name_plural': 'requisitions',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='requisition',
            unique_together=set([('request', 'description')]),
        ),
        migrations.AddField(
            model_name='material',
            name='request',
            field=models.ForeignKey(help_text=b'', to='requisitions.Requisition'),
            preserve_default=True,
        ),
    ]
