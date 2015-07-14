from django.contrib import admin
from .models import Process, Component, Prototype, Sap
from django.utils.translation import ugettext, ugettext_lazy as _
from actions import export_as_excel, export_as_csv
from sorl.thumbnail import get_thumbnail


class ComponentInline(admin.TabularInline):
	model = Component
	extra = 0

class ComponentAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('types of processes'), {'fields': ('code_component', 'code_sap',)}),
        (_('description and features'), {'fields': ('type_process', 'description',)}),
        (_('image support'), {'fields': ('image',)}),
        (None, {'fields': ('unit', 'active_component', 'created_component',)}),
    )
    list_display = ('code_component', 'type_process', 'code_sap', 'description', 'image_thumbnail', 'unit', 'active_component',)
    list_filter = ('type_process', 'unit', 'active_component',)
    search_fields = ['code_component', 'description', 'code_sap',]
    list_editable = ('unit', 'active_component',)
    readonly_fields = ('created_component',)

    actions = [export_as_excel, export_as_csv]

    # view image in the admin
    def image_thumbnail(self, obj):
        return '<img src="%s">' % get_thumbnail(obj.image, '50x50', format='PNG').url
    image_thumbnail.allow_tags = True
    image_thumbnail.admin_order_field = 'image'


class ProcessAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('types of processes'), {'fields': ('code_process',)}),
        (_('description and features'), {'fields': ('type_process', 'description',)}),
        (None, {'fields': ('active_process', 'created_process',)}),
    )
    list_display = ('code_process', 'description', 'type_process', 'active_process',)
    list_filter = ('type_process', 'active_process',)
    search_fields = ['code_process', 'description',]
    list_editable = ('active_process',)
    readonly_fields = ('created_process',)

    actions = [export_as_excel, export_as_csv]
    inlines = [ComponentInline]


class PrototypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('types of processes'), {'fields': ('code_prototype',)}),
        (_('description and features'), {'fields': ('type_prototype', 'format_prototype',)}),
        (_('model and make'), {'fields': ('model', 'make',)}),
        (_('features and color'), {'fields': ('seal_series', 'code_color',)}),
        (None, {'fields': ('active_prototype', 'created_prototype',)}),
    )
    list_display = ('code_prototype', 'created_prototype', 'type_prototype', 'model', 'make', 'seal_series', 'code_color', 'format_prototype', 'active_prototype',)
    list_filter = ('type_prototype', 'model', 'make', 'format_prototype', 'active_prototype',)
    search_fields = ['code_prototype', 'seal_series',]
    readonly_fields = ('created_prototype',)

    actions = [export_as_excel, export_as_csv]


class SapAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('types of processes'), {'fields': ('code_sap',)}),
        (_('description and features'), {'fields': ('description', 'type_sap',)}),
        (None, {'fields': ('active_sap', 'created_sap',)}),
    )
    list_display = ('code_sap', 'description', 'type_sap', 'created_sap', 'active_sap',)
    list_filter = ('type_sap', 'active_sap', 'created_sap',)
    search_fields = ['code_sap', 'description',]
    readonly_fields = ('created_sap',)

    actions = [export_as_excel, export_as_csv]


admin.site.register(Process, ProcessAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Prototype, PrototypeAdmin)
admin.site.register(Sap, SapAdmin)
