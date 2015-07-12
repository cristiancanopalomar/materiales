from django.contrib import admin
from .models import Component, Process

class ComponentAdmin(admin.ModelAdmin):
    pass

class ProcessAdmin(admin.ModelAdmin):
    pass

admin.site.register(Component, ComponentAdmin)
admin.site.register(Process, ProcessAdmin)
