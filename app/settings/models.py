from django.db import models

# Create your models here.
class Category(models.Model):
    logo = models.ImageField(
        upload_to="category/", 
        verbose_name="Логотип категории"
    )
    title = models.CharField(
        max_length=155, 
        verbose_name="Название категории"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class ProductImage(models.Model):
    image = models.ImageField(
        upload_to="product/", 
        verbose_name="Изображение товара"
    )

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"