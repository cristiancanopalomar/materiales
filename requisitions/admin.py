from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from .models import Requisition, Material, Agree, Reserve
from actions import export_as_excel, export_as_csv
from django.utils.translation import ugettext, ugettext_lazy as _


class MyFormSet(BaseInlineFormSet):
    def get_queryset(self):
        if not hasattr(self, '_queryset'):
            qs = super(
                MyFormSet,
                self
            ).get_queryset().filter(
                active=False,
                approved=True,
            )
            self._queryset = qs
        return self._queryset

class ReserveInline(admin.TabularInline):
    model = Material
    can_delete = False
    fields = ( 'code_sap', 'solicitude', 'generated', 'created_generated', 'center', 'warehouse', 'dispatched')
    raw_id_fields = ['center', 'warehouse',]
    readonly_fields = ('code_sap', 'solicitude', 'dispatched', 'created_generated',)
    extra = 0
    formset = MyFormSet
    autocomplete_lookup_fields = {
        'fk':[
            'center',
            'warehouse',
        ],
    }

class MaterialInline(admin.TabularInline):
    model = Material
    can_delete = False
    fields = ('request', 'code_sap', 'solicitude', 'created_solicitude', 'active', 'approved', 'dispatched')
    raw_id_fields = ['request', 'code_sap',]
    readonly_fields = ('created_solicitude', 'active', 'approved', 'dispatched',)
    extra = 0
    autocomplete_lookup_fields = {
        'fk':[
            'code_sap',
        ],
    }


class MaterialAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('request', 'code_sap',)}),
        (_('description and features'), {'fields': ('solicitude', 'created_solicitude', 'request_reserve',)}),
        (None, {'fields': ('active', 'approved', 'dispatched',)}),
    )
    list_display = ('request', 'code_sap', 'solicitude', 'generated', 'delivered', 'approved', 'dispatched',)
    list_filter = ('request', 'code_sap__code_sap', 'approved', 'dispatched',)
    search_fields = ['request', 'code_sap__code_sap', 'code_sap__description',]
    raw_id_fields = ['request', 'code_sap',]
    readonly_fields = ('active', 'approved', 'dispatched', 'created_solicitude', 'request_reserve',)
    autocomplete_lookup_fields = {'fk': ['request', 'code_sap',],}

    actions = [export_as_excel, export_as_csv]


class RequisitionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('request', 'conclude',)}),
        (_('description and features'), {'fields': ('description', 'created_requisition',)}),
    )
    list_display = ('request', 'description', 'created_requisition', 'conclude',)
    list_filter = ('created_requisition', 'conclude',)
    search_fields = ['request', 'description',]
    readonly_fields = ('request', 'conclude', 'created_requisition',)

    actions = [export_as_excel, export_as_csv]
    inlines = [MaterialInline]


class AgreeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('request', 'created_agree',)}),
        (_('description and features'), {'fields': ('material', 'description',)}),
    )
    list_display = ('request', 'description', 'created_agree',)
    list_filter = ('request', 'created_agree',)
    filter_horizontal = ('material',)
    search_fields = ['request', 'description',]
    readonly_fields = ('created_agree',)

    actions = [export_as_excel, export_as_csv]


class ReserveAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('request', 'reserve',)}),
        (_('description and features'), {'fields': ('order', 'sap_movement', 'sap_destination', 'division',)}),
        (_('support'), {'fields': ('support',)}),
        (None, {'fields': ('created_reserve', 'closing',)}),
    )
    list_display = ('request', 'reserve', 'order', 'sap_movement', 'sap_destination', 'created_reserve', 'closing',)
    list_filter = ('created_reserve', 'sap_movement', 'sap_destination', 'division', 'closing', 'order',)
    search_fields = ['request', 'reserve', 'order',]
    raw_id_fields = ['request', 'sap_movement', 'sap_destination', 'division',]
    readonly_fields = ('created_reserve', 'closing',)

    actions = [export_as_excel, export_as_csv]
    inlines = [ReserveInline]
    autocomplete_lookup_fields = {
        'fk':[
            'request',
            'sap_movement',
            'division',
            'sap_destination',
        ],
    }

admin.site.register(Requisition, RequisitionAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Agree, AgreeAdmin)
admin.site.register(Reserve, ReserveAdmin)
