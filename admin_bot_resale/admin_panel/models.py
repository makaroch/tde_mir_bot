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
    name = models.CharField(max_length=255, verbose_name="Название типа товара(что будет написано на кнопке)")

    class Meta:
        db_table = "products_types"
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продукта"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара(Что выведется при нажатии)", default="Позже появится")
    quantity = models.IntegerField(default=1, verbose_name="Кол-во в наличи")
    subtype = models.ForeignKey(to=ProductType, on_delete=models.PROTECT, verbose_name="Тип продукта")

    class Meta:
        db_table = "Product"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"Товар: {self.name}"
