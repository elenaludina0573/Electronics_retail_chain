from django.contrib import admin
from django.utils.html import format_html

from network.models import Factory, Retail, Individual, Product


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'country', 'city', 'address', 'phone_number']
    list_filter = ['country']
    actions = ['arrears_factory']


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'email', 'country', 'city', 'address', 'phone_number', 'arrears', 'product']
    list_filter = ['city']
    actions = ['arrears_factory']


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'email', 'country', 'city', 'address', 'phone_number', 'arrears', 'product']
    list_filter = ['city']
    actions = ['arrears_factory']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'model', 'release_date', 'created_at', 'factory']


@admin.action()
def arrears_factory(queryset):
    queryset.update(arrears=0)


def view_link(self, obj):
    """Ссылка на поставщика"""
    return format_html('<a href="{}">Просмотр поставщика</a>', obj.get_absolute_url())


view_link.short_description = 'Просмотр поставщика'
view_link.allow_tags = True
