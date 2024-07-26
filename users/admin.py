from django.contrib import admin
from .models import User, Seller, Admin, Client

admin.site.register(User)

admin.site.register(Admin)

admin.site.register(Seller)

admin.site.register(Client)