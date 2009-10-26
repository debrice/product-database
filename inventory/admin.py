from exceptions import ValueError
import csv
from datetime import datetime


from django.contrib import admin
from django import forms


from models import Inventory, Warehouse, Import
from product.models import Product

class InventoryAdmin(admin.ModelAdmin):
    search_fields = ('product__item_number',)
    list_display = ('warehouse', 'product', 'quantity', 'modification_date')
    list_filter = ('warehouse', )

class InventoryInline(admin.TabularInline):
    model = Inventory
    extra = 0

class WarehouseAdmin(admin.ModelAdmin):
    search_fields = ('title', 'ref')
    list_display = ('ref', 'title',)

class ImportAdminForm(forms.ModelForm):
    search_fields = ('title',)
    list_filter = ('is_imported', 'import_date', )
    class Meta:
        exclude = ('is_imported', 'import_date', 'updated_product', 'created_product')

class ImportAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title', 'creation_date', 'modification_date', 'is_imported', 'import_date',)
    list_filter = ('is_imported', 'import_date')
    form = ImportAdminForm


admin.site.register(Import, ImportAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
