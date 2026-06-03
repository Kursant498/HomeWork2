from django.db import models
from ckeditor.fields import RichTextField
from app.product.enum import RATING, DISCOUNT
from app.settings.models import Category
# Create your models here.

class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        verbose_name="Категория товара"
    )
    title = models.CharField(
        max_length=155, 
        verbose_name="Название товара"
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Цена товара"
    )
    description = RichTextField(
        verbose_name="Описание товара"
    )
    image1 = models.ImageField(
        upload_to="product/", 
        verbose_name="Изображение товара"
    )
    image2 = models.ImageField(
        upload_to="product/", 
        verbose_name="Изображение товара"
    )
    image3 = models.ImageField(
        upload_to="product/", 
        verbose_name="Изображение товара"
    )
    rating = models.CharField(
        max_length=20,
        verbose_name="Рейтинг товара",
        choices=RATING
    )
    discount = models.CharField(
        max_length=20,
        verbose_name="Скидка на товар",
        choices=DISCOUNT
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания товара"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
