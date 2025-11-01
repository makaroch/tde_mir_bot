from django.contrib import admin
from .models import Client, ProductType, Product


#
# class ProductTabAdmin(admin.TabularInline):
#     model = Product
#     fields = ("name", "price", "quantity", "subtype")
#     search_fields = ("name", "price", "quantity", "subtype")
#     readonly_fields = ("name",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("tg_user_id", "username", "is_subscription",)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "subtype", "quantity",)
    search_fields = ("name", "description", "subtype", "quantity",)
    list_filter = ("subtype",)
    fields = (
        "name",
        "description",
        "quantity",
        "subtype",
    )
    list_per_page = 30
