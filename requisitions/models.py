from django.db import models
from basics.models import Component
from basics.rename import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class Requisition(models.Model):
    request = models.CharField(
        max_length=20,
        primary_key=True,
        unique=True,
        default=random()
    )
    created_requisition = models.DateTimeField(
        auto_now_add=True,
    )
    description = models.TextField(
        help_text='description of the requisition',
    )
    conclude = models.BooleanField(
        default=False,
    )

    class Meta:
        unique_together = ('request', 'description')
        verbose_name = u'requisition'
        verbose_name_plural = u'requisitions'

    def __unicode__(self):
        return unicode(self.request)


class Material(models.Model):
    request = models.ForeignKey(
        Requisition,
        help_text='request number',
    )
    code_sap = models.ForeignKey(
        Component,
        help_text='sap basic model code',
    )
    solicitude = models.DecimalField(
        _('quantity applied'),
        max_digits=7,
        decimal_places=2,
        default=0,
    )
    created_solicitude = models.DateTimeField(
        _('creation date'),
        auto_now_add=True,
        help_text='item creation date',
    )
    generated = models.DecimalField(
        _('quantity generated'),
        max_digits=7,
        decimal_places=2,
        default=0,
    )
    created_generated = models.DateTimeField(
        _('creation date'),
        null=True,
        help_text='item creation date',
    )
    delivered = models.DecimalField(
        _('quantity delivered'),
        max_digits=7,
        decimal_places=2,
        default=0,
    )
    created_delivered = models.DateTimeField(
        _('creation date'),
        null=True,
        help_text='item creation date',
    )
    approved = models.BooleanField(
        default=False,
    )
    active = models.BooleanField(
        default=True,
    )
    dispatched = models.BooleanField(
        default=False,
    )

    class Meta:
        unique_together = ('request', 'code_sap')
        verbose_name = u'requested material'
        verbose_name_plural = u'requested material'

    def __unicode__(self):
        return unicode(self.code_sap)


class Agree(models.Model):
    request = models.ForeignKey(
        Requisition,
        primary_key=True,
        unique=True,
    )
    material = models.ManyToManyField(
        Material,
        limit_choices_to={
            'approved': False,
            'active': True,
        }
    )
    description = models.TextField()
    created_agree = models.DateTimeField(
        _('creation date'),
        auto_now_add=True,
        help_text='item creation date',
    )

    class Meta:
        unique_together = ('request',)
        verbose_name = u'accept request'
        verbose_name_plural = u'accept request'

    def algo(self, obj):
        return obj.material

    def __unicode__(self):
        return unicode(self.request)


@receiver(post_save, sender=Agree)
def send_notification(sender, instance, created, **kwargs):
    if created:
        a = Agree.objects.all().values_list('material', flat=True)
        print a

        approve_order = Agree.objects.all().values_list(
            'material',
            flat=True,
        ).filter(
            request=20150717162413,
        )
        print approve_order
        user_group = Agree.objects.all().values_list('material', flat=True)
        print type(user_group)
        print user_group
        # Material.objects.filter(
        #     request=(
        #         instance,
        #     ),
        #     id__in=(
        #         list(approve_order),
        #     )
        # ).update(
        #     active=False,
        #     approved=True,
        # )
