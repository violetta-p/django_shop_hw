from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, categories, filtered_items

app_name = CatalogConfig.name

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name="product_list"),
    path('contacts/', contacts, name="contacts"),
    path('products/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('products/view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('', categories, name="categories"),
    path('<int:pk>/items/', filtered_items, name="filtered_items"),

]
