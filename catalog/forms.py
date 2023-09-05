from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'category', 'price', 'preview_pic')

    def clean_name(self):
        forbidden_items = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                           'бесплатно', 'обман', 'полиция', 'радар', 'casino', 'cryptocurrency',
                           'crypt', 'exchange', 'cheap', 'free', 'fraud', 'police', 'radar']
        cleaned_data = self.cleaned_data['title']
        for item in forbidden_items:
            if item in cleaned_data.lower():
                raise forms.ValidationError(f'The word "{item}" cannot be used in the product name.')
        return cleaned_data

    def clean_description(self):
        forbidden_items = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                           'бесплатно', 'обман', 'полиция', 'радар', 'casino', 'cryptocurrency',
                           'crypt', 'exchange', 'cheap', 'free', 'fraud', 'police', 'radar']
        cleaned_data = self.cleaned_data['description']
        for item in forbidden_items:
            if item in cleaned_data.lower():
                raise forms.ValidationError(f'The word "{item}" cannot be used in the product description.')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'
