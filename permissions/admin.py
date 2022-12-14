from django.contrib import admin
from django.utils.html import format_html
from datetime import date

from .models import City, Permission, Registration

# Register your models here.

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'phone', 'email')


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


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'city', 'expiration_date', 'get_status')
    search_fields = ['registration_number', 'city__name']
    ordering = ['expiration_date']
    list_filter = ('city', StatusFilter)

    def get_status(self, registration):
        if date.today() > registration.expiration_date:
            return format_html("<div style='color:red'><b>Expired</b></div>")
        else:
            return format_html("<div style='color:green'><b>Active</b></div>")

    get_status.short_description = "status"

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('permission_number', 'po', 'address', 'get_city', 'status', 'permission_document')
    list_filter = ('status','registration__city')

    def get_form(self, request, obj=None, **kwargs):
        form = super(PermissionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['registration'].queryset = Registration.objects.filter(expiration_date__gte=date.today())
        return form
    
    def get_city(self, permission):
        return permission.registration.city

    get_city.short_description = "city"