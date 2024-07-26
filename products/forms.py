from django import forms
from .models import Product, Cart

# Edit qilish uchun form

class ProductEditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    description = forms.CharField(widget=forms.Textarea({"class": "form-control"}))
    price = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    quantity = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control"}))
    class Meta:
        model = Product
        fields = ('name','price','quantity','description','image','category')


# Create qilish uchun fomr

class ProductCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    price = forms.IntegerField(widget=forms.TextInput({"class": "form-control"}))
    quantity = forms.IntegerField(widget=forms.TextInput({"class": "form-control"}))
    description = forms.CharField(widget=forms.Textarea({"class": "form-control"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control"}))
    class Meta:
        model = Product
        fields = ('name','price','quantity','description','image','category')


class SavatchaEditForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.TextInput({"class": "form-control"}))
    class Meta:
        model = Cart
        fields = ('quantity',)