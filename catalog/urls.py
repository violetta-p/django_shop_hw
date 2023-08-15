from django.urls import path
#from catalog.views import home_page_controller, contacts_controller
from catalog import views
import os

urlpatterns = [
    path('', views.home_page_controller, name="home_page_controller"),
    path('contacts/', views.contacts_controller, name="contacts_controller"),
]
