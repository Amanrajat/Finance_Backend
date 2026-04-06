from django.contrib import admin
from .models import Summary


@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'total_income',
        'total_expense',
        'balance',
        'last_updated'
    )

    search_fields = ('user__email',)
    ordering = ('-last_updated',)

    readonly_fields = ('id', 'last_updated')

    fieldsets = (
        ('User Info', {
            'fields': ('id', 'user')
        }),
        ('Financial Summary', {
            'fields': ('total_income', 'total_expense', 'balance')
        }),
        ('System Info', {
            'fields': ('last_updated',)
        }),
    )