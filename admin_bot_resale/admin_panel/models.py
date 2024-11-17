from django.db import models



class Client(models.Model):
    tg_user_id = models.BigIntegerField(verbose_name="Телеграм id")
    username = models.CharField(max_length=255, verbose_name="Username")
    is_subscription = models.BooleanField(default=True, verbose_name="Подписан на рассылку")

    class Meta:
        db_table = "clients"
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"Клиент: {self.username} | {self.tg_user_id}"


class ProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название типа товара")

    class Meta:
        db_table = "products_types"
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продукта"

    def __str__(self):
        return f"Тип продукта: {self.name}"


class ManufacturerCompany(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название фирмы товара")

    class Meta:
        db_table = "manufacturer_companies"
        verbose_name = "Фирма производитель"
        verbose_name_plural = "Фирмы производитель"

    def __str__(self):
        return f"Фирма производитель: {self.name}"


class Subtype(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название подтипа")
    products_type = models.ForeignKey(to=ProductType, on_delete=models.PROTECT, verbose_name="Тип продукта")
    manufacturer_company = models.ForeignKey(to=ManufacturerCompany, on_delete=models.PROTECT,
                                             verbose_name="Фирма производитель")

    def __str__(self):
        return f"Подтип: {self.name}"

    class Meta:
        db_table = "Subtype"
        verbose_name = "Подтип"
        verbose_name_plural = "Подтипы"

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    price = models.IntegerField(verbose_name="Цена")
    quantity = models.IntegerField(default=1, verbose_name="Кол-во в наличи")
    subtype = models.ForeignKey(to=Subtype, on_delete=models.PROTECT, verbose_name="Подтип")

    class Meta:
        db_table = "Product"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"Товар: {self.name}"
