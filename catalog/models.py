from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview_pic = models.ImageField(upload_to='project_pictures/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'Категория: {self.category} ' \
               f'Наименование: {self.product_name} ' \
               f'Описание: {self.description}' \
               f'Цена: {self.price}' \
               f'Дата создания: {self.creation_date} ' \
               f'Дата изменения: {self.modified_date}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('modified_date',)


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'
