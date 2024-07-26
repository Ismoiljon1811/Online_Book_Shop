from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import LoginForm, RegisterForm, CreateSellerForm, UpdateSellerForm
from .permissions import AdminRequiredMixin, SellerRequiredMixin
from .models import Client, Admin, Seller, User






class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user.user_role == 'student':
                new_student = Client()
                new_student.user = user
                new_student.save()

            return redirect('/')
        return render(request, 'users/register.html', {'form': form})
    

class AdminDashboardView(AdminRequiredMixin,View):
    def get(self,request):
        return render(request,'users/admin.html')
    

class SellerView(AdminRequiredMixin, View):
    def get(self, request):
        form = CreateSellerForm()
        return render(request, 'users/seller_create.html', {'form': form})


    def post(self, request):
        form = CreateSellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:admin')
        return render(request, 'users/seller_create.html', {'form': form})
    

class SellerEditView(AdminRequiredMixin,View):
    def get(self,request):
        sellers = Seller.objects.all()
        return render(request,'users/seller_edit.html',{"sellers":sellers})


class UpdateSellerView(AdminRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User,id=id)
        form = UpdateSellerForm(instance=user)
        return render(request, 'users/seller_update.html', {'form': form})


    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UpdateSellerForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:admin')
        return render(request, 'users/seller_update.html', {'form': form})


class DeleteSellerView(AdminRequiredMixin, View):
    def get(self, request, id):
        seller = Seller.objects.get(id=id)
        seller.delete()
        return redirect('users:admin')





