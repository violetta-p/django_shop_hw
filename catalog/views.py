from django.shortcuts import render


def home_page_controller(request):
    return render(request, 'catalog/home_page.html')


def contacts_controller(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name, email)
    return render(request, 'catalog/contacts.html')
