from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.phone, name='phone'),
    path('products/<str:pk>/', views.filterphone, name='phone'),
    path('products/<slug:pk>/', views.product_detail, name='phone'),
    path('products/<str:br>/<slug:pk>/', views.product_detail, name='phone'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
]