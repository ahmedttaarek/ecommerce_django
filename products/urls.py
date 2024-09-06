from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),  # Path for welcome view
    path('products/', views.product_list, name='product_list'),  # Path for product list view
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # Path for product detail view
    path('login/', views.login_view, name='login'),  # Path for login view
]
