from django.urls import path
from .views import LoginView, RegisterView, AdminDashboardView, SellerView, SellerEditView, UpdateSellerView, LogoutView, DeleteSellerView

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', AdminDashboardView.as_view(), name='admin'),
    path('seller-create/', SellerView.as_view(), name='seller_create'),
    path('seller-edit/', SellerEditView.as_view(), name='seller_edit'),
    path('seller-update/<int:id>', UpdateSellerView.as_view(), name='seller_update'),
    path('seller-delete/<int:id>', DeleteSellerView.as_view(), name='seller_delete'),
]