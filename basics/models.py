from django.db import models
from .rename import rename_file

class Process(models.Model):
    type_code = (
        ('M', 'material'),
        ('A', 'activity'),
    )
    code_process = models.PositiveIntegerField()
    description = models.CharField(
        max_length=15,
        help_text='description of the material or activity',
    )
    type_process = models.CharField(
        max_length=1,
        choices=type_code,
    )
    active_process = models.BooleanField(
        default=True
    )

    class Meta:
        unique_together = ('code_process', 'type_process')
        verbose_name = u'code [process - activity]'
        verbose_name_plural = u'code [process - activity]'

    def __unicode__(self):
        return unicode(self.description)


class Component(models.Model):
    type_unit = (
        ( 'M', 'meters'),
        ('CU', 'units' ),
    )
    type_process = models.ForeignKey(
        'Process',
        limit_choices_to={
            'type_process': 'M',
        },
    )
    code_component = models.PositiveIntegerField(
        unique=True,
    )
    code_sap = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
        help_text='material code (trading system SAP)',
    )
    description = models.CharField(
        max_length=100,
        help_text='description of the Component',
    )
    image = models.ImageField(
        upload_to=rename_file(
            'upload/basic/component',
        ),
    )
    unit = models.CharField(
        max_length=2,
        choices=type_unit,
    )
    active_component = models.BooleanField(
        default=True,
    )

    class Meta:
        unique_together = ('code_component', 'code_sap', 'description')
        verbose_name = u'component not serialized'
        verbose_name_plural = u'component not serialized'

    def __unicode__(self):
        return unicode(self.description)
