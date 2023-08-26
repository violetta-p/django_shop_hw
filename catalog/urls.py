from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('contacts/', contacts, name="contacts"),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
]
