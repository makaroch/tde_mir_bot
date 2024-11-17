from django.contrib import admin
from .models import Client, ProductType, ManufacturerCompany, Product, Subtype


class ProductTabAdmin(admin.TabularInline):
    model = Product
    fields = ("name", "price", "quantity", "subtype")
    search_fields = ("name", "price", "quantity", "subtype")
    readonly_fields = ("name", )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("tg_user_id", "username", "is_subscription",)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ManufacturerCompany)
class ManufacturerCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "subtype")
    list_editable = ("price", "quantity")
    search_fields = ("name", "price", "quantity",)
    list_filter = ("subtype", )
    fields = (
        "name",
        ("price", "quantity"),
        "subtype"
    )
    list_per_page = 30


@admin.register(Subtype)
class SubtypeAdmin(admin.ModelAdmin):
    list_display = ("name", "products_type", "manufacturer_company")
    list_filter = ("products_type", "manufacturer_company")

    inlines = [ProductTabAdmin, ]

    list_per_page = 30