from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from catalog.models import Product, Category, Version
from catalog.forms import ProductForm, VersionForm
from catalog.services import get_categories_cache


class ProductListView(ListView):
    model = Product
    paginate_by = 12


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):

    model = Product
    form_class = ProductForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator == self.request.user or self.request.user.is_superuser:
            return self.object
        else:
            raise Http404


    def get_success_url(self):
        return reverse('catalog:product_edit', args=[self.kwargs.get('pk')])
    #success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        active_versions = Version.objects.filter(product=self.object, is_active=True)
        if active_versions.count() > 1:
            form.add_error(None, 'Choose one active version.')
            return self.form_invalid(form)
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator == self.request.user or self.request.user.is_superuser:
            return self.object
        else:
            raise Http404


def categories(request):
    content = {
        'category_list': get_categories_cache(),
    }
    return render(request, 'catalog/categories.html', content)


def filtered_items(request, pk):
    category_item = Category.objects.get(pk=pk)
    content = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{category_item.name}',
        'description': f'{category_item.description}'
    }
    return render(request, 'catalog/filtered_items.html', content)
