from django.urls import path
from catalog.views import home_page_controller, contacts_controller

urlpatterns = [
    path('', home_page_controller),
    path('', contacts_controller)
]
