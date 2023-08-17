from django.contrib import admin
from catalog.models import Product, Category

#admin.site.register(Category)
#admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category_id')
    list_filter = ('category',)
    search_fields = ('product_name', 'description', )
