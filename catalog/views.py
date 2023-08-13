from django.shortcuts import render


def home_page_controller(request):
    return render(request, 'catalog/home_page.html')


def contacts_controller(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')
