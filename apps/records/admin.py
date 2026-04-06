from django.contrib import admin
from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'amount',
        'type',
        'category',
        'date',
        'created_at'
    )

    list_filter = ('type', 'category', 'date')
    search_fields = ('category', 'note', 'user__email')

    ordering = ('-created_at',)

    readonly_fields = ('id', 'created_at')

    fieldsets = (
        ('Basic Info', {
            'fields': ('id', 'user')
        }),
        ('Transaction Details', {
            'fields': ('amount', 'type', 'category', 'date')
        }),
        ('Additional Info', {
            'fields': ('note',)
        }),
        ('System Info', {
            'fields': ('created_at',)
        }),
    )