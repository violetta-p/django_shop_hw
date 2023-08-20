from django.shortcuts import render
from catalog.models import Product, Category

# def home_page_controller(request):
#     return render(request, 'catalog/home_page.html')

def home_page(request):
    products_all = Product.objects.all()
    category_all = Category.objects.all()
    content = {
        'objects_list': products_all,
        'category_list': category_all,
        'title': 'Skystore',
    }
    return render(request, 'catalog/home_page.html', content)

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

