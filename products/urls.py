from django.urls import path
from .views import home, category, Batafsil, SellerDashboardView, AllProductsTableView, ProductEditView, ProductCreateView, DeleteProductView, Savatcha
from .views import SavatchaEditView, DeleteSavatchaView


app_name = 'products'


urlpatterns = [
    path('category/<int:id>/', category, name="category"),
    path('batafsil/<int:id>/',Batafsil.as_view(),name='batafsil'),
    path('seller/', SellerDashboardView.as_view(),name='seller'),
    path('all-products-table/', AllProductsTableView.as_view(),name='all_products_table'),
    path('edit-product/<int:id>/', ProductEditView.as_view(), name='edit_product'),
    path('edit-savatcha/<int:id>/', SavatchaEditView.as_view(), name='edit_savatcha'),
    path('create-product/', ProductCreateView.as_view(), name='create_product'),
    path('delete-product/<int:id>/', DeleteProductView.as_view(), name='delete_product'),
    path('delete-savatcha/<int:id>/', DeleteSavatchaView.as_view(), name='delete_savatcha'),
    path('savatcha/', Savatcha.as_view(), name='savatcha'),
]