from django.contrib import admin

from .models import Attribute


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('name', 'families')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
