from django.contrib import admin
from .models import Process, Component
from django.utils.translation import ugettext, ugettext_lazy as _
from actions import export_as_excel, export_as_csv
from sorl.thumbnail import get_thumbnail

class ProcessAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('types of processes'), {'fields': ('code_process',)}),
        (_('description and features'), {'fields': ('type_process', 'description',)}),
        (None, {'fields': ('active_process',)}),
    )
    list_display = ('code_process', 'description', 'type_process', 'active_process',)
    list_filter = ('type_process', 'active_process',)
    search_fields = ['code_process', 'description',]
    list_editable = ('active_process',)
    actions = [export_as_excel, export_as_csv]


class ComponentAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('types of processes'), {'fields': ('code_component', 'code_sap',)}),
        (_('description and features'), {'fields': ('type_process', 'description',)}),
        (_('image support'), {'fields': ('image',)}),
        (None, {'fields': ('unit', 'active_component',)}),
    )
    list_display = ('code_component', 'type_process', 'code_sap', 'description', 'image_thumbnail', 'unit', 'active_component',)
    list_filter = ('type_process', 'unit', 'active_component',)
    search_fields = ['code_component', 'description', 'code_sap',]
    list_editable = ('unit', 'active_component',)
    actions = [export_as_excel, export_as_csv]

    def image_thumbnail(self, obj):
        return '<img src="%s">' % get_thumbnail(obj.image, '50x50', format='PNG').url
    image_thumbnail.allow_tags = True

admin.site.register(Process, ProcessAdmin)
admin.site.register(Component, ComponentAdmin)
