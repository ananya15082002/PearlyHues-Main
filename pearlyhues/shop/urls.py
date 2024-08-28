from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product_details, name='product_details'),
    path('bracelets/', views.bracelet_and_rings, name='bracelet_and_rings'),
    path('earrings/', views.earrings, name='earrings'),
    path('necklaces/', views.necklace, name='necklace'),
    path('cart/', views.cart_address, name='cart_address'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('new-account/', views.new_account, name='new_account'),
]
