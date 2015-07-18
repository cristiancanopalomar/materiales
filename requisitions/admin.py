from django.contrib import admin
from .models import Requisition, Material, Agree
from actions import export_as_excel, export_as_csv
from django.utils.translation import ugettext, ugettext_lazy as _


class MaterialInline(admin.TabularInline):
    model = Material
    can_delete = False
    fields = ('request', 'code_sap', 'solicitude', 'created_solicitude', 'active', 'approved', 'dispatched')
    raw_id_fields = ['request', 'code_sap',]
    readonly_fields = ('created_solicitude', 'active', 'approved', 'dispatched',)
    extra = 0

class MaterialAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('request', 'code_sap',)}),
        (_('description and features'), {'fields': ('solicitude', 'created_solicitude',)}),
        (None, {'fields': ('active', 'approved', 'dispatched',)}),
    )
    list_display = ('request', 'code_sap', 'solicitude', 'generated', 'delivered', 'approved', 'dispatched',)
    list_filter = ('request', 'code_sap__code_sap', 'approved', 'dispatched',)
    search_fields = ['request', 'code_sap__code_sap', 'code_sap__description',]
    raw_id_fields = ['request', 'code_sap',]
    readonly_fields = ('active', 'approved', 'dispatched', 'created_solicitude',)

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


admin.site.register(Requisition, RequisitionAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Agree, AgreeAdmin)
