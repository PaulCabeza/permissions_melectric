from django.contrib import admin
from django.utils.html import format_html
from datetime import date

from .models import State, City, Permission

# Register your models here.

admin.site.register(State)
admin.site.register(City)
# admin.site.register(Permission)

class StatusFilter(admin.SimpleListFilter):
    title = 'Status Filter'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('is_active', 'Active'),
            ('is_expired', 'Expired')
        )

    def queryset(self, request, queryset):
        if self.value() == 'is_expired':
            return queryset.filter(expiration_date__lte=date.today())
        elif self.value() == 'is_active':
            return queryset.filter(expiration_date__gte=date.today())

        return queryset


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('permission_number', 'city', 'expiration_date', 'get_status')
    search_fields = ['permission_number', 'city__name']
    ordering = ['expiration_date']
    list_filter = ('city', StatusFilter)

    def get_status(self, permission):
        if date.today() > permission.expiration_date:
            return format_html("<div style='color:red'><b>Expired</b></div>")
        else:
            return "OK"

    get_status.short_description = "status"