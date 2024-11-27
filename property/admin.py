"""
    Registering Property and PropertyImage models to the admin panel.
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Property, PropertyImage


# Register your models here.

@admin.register(Property)
class PropertyAdmin(SummernoteModelAdmin):
    """
        Registering the Property model to the admin panel.
        Setting what is displayed in the admin panel.
        Along with other options.
    """
    list_display = ('title', 'owner', 'status', 'created_on', )
    list_filter = ('status', 'created_on', )
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_on'
    ordering = ['status', 'created_on']
    summernote_fields = ('description', )
    list_editable = ('status',)
    list_display_links = ('title', 'owner', )


admin.site.register(PropertyImage)
