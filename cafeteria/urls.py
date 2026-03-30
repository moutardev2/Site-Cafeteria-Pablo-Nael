"""
URL configuration for cafeteria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_cas_ng import views as cas_views
from cafeteria_app.views import (
    home,
    product_add,
    product_delete,
    product_edit,
    product_list,
    product_manage_list,
    student_add,
    student_delete,
    student_edit,
    student_list,
    transaction_add,
    transaction_delete,
    transaction_edit,
    transaction_list,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', cas_views.LoginView.as_view(), name='cas_ng_login'),
    path('accounts/logout/', cas_views.LogoutView.as_view(), name='cas_ng_logout'),
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/manage/', product_manage_list, name='product_manage_list'),
    path('products/add/', product_add, name='product_add'),
    path('products/<int:pk>/edit/', product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
    path('students/', student_list, name='student_list'),
    path('students/add/', student_add, name='student_add'),
    path('students/<int:pk>/edit/', student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),
    path('transactions/', transaction_list, name='transaction_list'),
    path('transactions/add/', transaction_add, name='transaction_add'),
    path('transactions/<int:pk>/edit/', transaction_edit, name='transaction_edit'),
    path('transactions/<int:pk>/delete/', transaction_delete, name='transaction_delete'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
