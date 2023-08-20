from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home_page, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name="home_page"),
    path('contacts/', contacts, name="contacts"),
]
