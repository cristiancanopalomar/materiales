from django.db import models

class Process(models.Model):
    type_code = (
        ('M', 'material'),
        ('A', 'activity'),
    )
    code = models.PositiveIntegerField()
    description = models.CharField(
        max_length=15,
        help_text='description of the material or activity',
    )
    type_process = models.CharField(
        max_length=1,
        choices=type_code,
    )
    active = models.BooleanField(
        default=True
    )

    class Meta:
        unique_together = ('code', 'type_process')
        verbose_name = u'code [process - activity]'
        verbose_name_plural = u'code [process - activity]'

    def __unicode__(self):
        return unicode(self.description)
