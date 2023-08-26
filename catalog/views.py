from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from catalog.models import Product, Category

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    content = {
        'title': 'Contacts',
    }
    return render(request, 'catalog/contacts.html', content)

class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'category', 'price', 'preview_pic')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'description', 'price', 'preview_pic')
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
