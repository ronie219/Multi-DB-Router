from django.contrib.auth.views import (LoginView ,
                                        LogoutView,
                                        LogoutView)
from django.contrib import admin
from django.urls import path

from .views import UserCreation,Home,ProductCreation,ProductList,UserList,deleteProduct,editProduct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('createuser/',UserCreation,name='account-creation'),
    path('login/', LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),
    path('createproduct/',ProductCreation,name='product-creation'),
    path('productlist/',ProductList, name='product-list'),
    path('userslist/',UserList,name = 'user-list'),
    path('deleteproduct/<pk>/<db>/',deleteProduct,name='delete-product'),
    path('editproduct/<pk>/<db>/<name>/',editProduct,name='edit-product')
]
