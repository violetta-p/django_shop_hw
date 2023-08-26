from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    preview_pic = models.ImageField(upload_to='project_pictures/', **NULLABLE, verbose_name='Picture')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Price(rub)')
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} {self.price}' \
               f'Описание: {self.description}' \

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('modified_date',)


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'
