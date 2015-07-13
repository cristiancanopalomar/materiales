from django.contrib import admin
from .models import Process, Component, Prototype
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
        (None, {'fields': ('unit', 'active_component',)}),
    )
    list_display = ('code_component', 'type_process', 'code_sap', 'description', 'image_thumbnail', 'unit', 'active_component',)
    list_filter = ('type_process', 'unit', 'active_component',)
    search_fields = ['code_component', 'description', 'code_sap',]
    list_editable = ('unit', 'active_component',)
    actions = [export_as_excel, export_as_csv]

    # view image in the admin
    def image_thumbnail(self, obj):
        return '<img src="%s">' % get_thumbnail(obj.image, '50x50', format='PNG').url
    image_thumbnail.allow_tags = True
    

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

    inlines = [ComponentInline]

class PrototypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('types of processes'), {'fields': ('code_prototype',)}),
        (_('description and features'), {'fields': ('type_prototype', 'format_prototype',)}),
        (_('model and make'), {'fields': ('model', 'make',)}),
        (_('features and color'), {'fields': ('seal_series', 'code_color',)}),
        (None, {'fields': ('active_prototype',)}),
    )
    list_display = ('code_prototype', 'type_prototype', 'model', 'make', 'seal_series', 'code_color', 'format_prototype', 'active_prototype',)
    list_filter = ('type_prototype', 'model', 'make', 'format_prototype', 'active_prototype',)
    search_fields = ['code_prototype', 'seal_series',]
    actions = [export_as_excel, export_as_csv]


admin.site.register(Process, ProcessAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Prototype, PrototypeAdmin)
