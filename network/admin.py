from django.contrib import admin

from network.models import Factory, Retail, Individual, Product


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'country', 'city', 'address', 'phone_number']


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'email', 'country', 'city', 'address', 'phone_number', 'arrears', 'product']


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'email', 'country', 'city', 'address', 'phone_number', 'arrears', 'product']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'model', 'release_date', 'created_at']
