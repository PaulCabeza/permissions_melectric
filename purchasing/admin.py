from django.contrib import admin
from datetime import date
from .models import Client, PurchaseOrder
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'client', 'get_client_address', 'status')
    list_filter = ('status',)

    def get_client_address(self, purchase_order):
        client_address = purchase_order.client.address
        return client_address
    get_client_address.short_description = "Client Address"

    def get_form(self, request, obj=None, **kwargs):
        form = super(PurchaseOrderAdmin, self).get_form(request, obj, **kwargs)
        current_year = str(date.today().year)[-2:]
        current_month = date.today().month
        if len(str(current_month)) == 1:
            current_month = "0" + str(current_month)
        else:
            current_month = str(current_month)

        last_po = PurchaseOrder.objects.all().last()
        if last_po:
            last_po_number = int(last_po.number[-2:]) + 1
            if len(str(last_po_number)) == 1:
                new_po_number = "0" + str(last_po_number)
            else:
                new_po_number = str(last_po_number)
            
        else:
            new_po_number = '01'

        new_po_number = str(current_year) + '-' + current_month + new_po_number

        form.base_fields['number'].initial = new_po_number
        return form
