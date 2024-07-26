from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Category, Cart
from users.permissions import SellerRequiredMixin
from .forms import ProductEditForm, ProductCreateForm, SavatchaEditForm

# Home page

def home(request):
    products = Product.objects.filter(in_stock = True)
    categorys = Category.objects.all()
    count = Cart.objects.filter(quantity__gt = 0).count()
    return render(request, 'base.html', {"products":products, "cats":categorys,'count':count})



def category(request, id):
    cat = get_object_or_404(Category, id=id)
    products = cat.products.all()
    categorys = Category.objects.all()
    count = Cart.objects.filter(quantity__gt = 0).count()
    return render(request, 'base.html', {"products": products, "cats":categorys,'count':count})

# Batafsil page uchun

class Batafsil(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        categorys = Category.objects.all()
        count = Cart.objects.filter(quantity__gt = 0).count()
        return render(request, 'products/batafsil.html', {"product": product, "cats":categorys,'count':count})
    
    def post(self,request,id):
        product = get_object_or_404(Product,id = id)
        products = Product.objects.filter(id=id).first()
        quantity = int(request.POST['cart'])

        if quantity != 0:
            if Cart.objects.filter(product = product).exists():
                cart = Cart.objects.filter(product=product).first()
                cart.quantity += quantity
                cart.save()

            else:
                cart = Cart()
                cart.product = product
                cart.quantity = quantity
                cart.save()
            products.quantity = products.quantity - quantity
            products.save()
            return redirect(home)
    
# Yangi Seller uchun olingan dashboard uchun

class SellerDashboardView(SellerRequiredMixin,View):
    def get(self,request):
        products = Product.objects.all()
        return render(request,'products/seller.html',{'products':products})
    

# Hamma productlar chiqadigan view (Seller uchun, jadval ko'rinishida)

class AllProductsTableView(SellerRequiredMixin,View):
    def get(self,request):
        products = Product.objects.all()
        return render(request,'products/all_products_table.html',{'products':products})
    

# Edit yani Update qilish (Seller tomonidan)

class ProductEditView(SellerRequiredMixin,View):
    def get(self, request, id):
        student = get_object_or_404(Product, id=id)
        form = ProductEditForm(instance=student)
        return render(request, 'products/edit_product.html', {'form': form})

    def post(self, request, id):
        student = get_object_or_404(Product, id=id)
        form = ProductEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('products:all_products_table')
        form = ProductEditForm(instance=student)
        return render(request, 'products/edit_product.html', {'form': form})
    
# Cread (Seller tomonidan Product qo'shish)
    

class ProductCreateView(SellerRequiredMixin,View):
    def get(self, request):
        form = ProductCreateForm()
        return render(request, 'products/create_product.html', {'form': form})

    def post(self, request):
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:all_products_table')
        form = ProductCreateForm()
        return render(request, 'products/create_product.html', {'form': form})



# Delete (Seller tomindan Productni)
    
class DeleteProductView(SellerRequiredMixin, View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('products:all_products_table')
    
# Savatcha tabli uchun cartlar

class Savatcha(View):
    def get(self,request):
        carts = Cart.objects.all()
        count = Cart.objects.filter(quantity__gt = 0).count()
        return render(request,'products/savatcha.html',{'carts':carts,'count':count})
    

# savatchadagi mahsulotni edit qilish yani olinayotgan mahsulot sonini

class SavatchaEditView(View):
    def get(self, request, id):
        student = get_object_or_404(Cart, id=id)
        form = SavatchaEditForm(instance=student)
        count = Cart.objects.filter(quantity__gt = 0).count()
        return render(request, 'products/edit_savatcha.html', {'form': form})

    def post(self, request, id):
        student = get_object_or_404(Cart, id=id)
        form = SavatchaEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('products:savatcha')
        form = SavatchaEditForm(instance=student)
        return render(request, 'products/edit_savatcha.html', {'form': form})
    

# Savatchadagi malumotni buyurmani o'chirib yuborish

class DeleteSavatchaView(View):
    def get(self, request, id):
        cart = Cart.objects.get(id=id)
        product = Product.objects.filter(id=cart.product.id).first()
        carts = cart.quantity
        product.quantity = product.quantity + carts
        product.save()
        cart.delete()
        return redirect('products:savatcha')