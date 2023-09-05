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
        return f'{self.product_name} {self.price}' \
               f'Description: {self.description}' \


    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('modified_date',)


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='category name')
    description = models.TextField(verbose_name='category description', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='product')
    version_number = models.PositiveSmallIntegerField(verbose_name='version number')
    version_name = models.CharField(max_length=100, verbose_name='version name')
    is_active = models.BooleanField(verbose_name='flag of the current version')

    def __str__(self):
        return f'{self.version_number}: {self.version_name}'

    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'
