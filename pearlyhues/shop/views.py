from django.shortcuts import render


def index(request):
    return render(request, 'shop/index.html')

def product_details(request):
    return render(request, 'shop/SingleProduct.html')

def bracelet_and_rings(request):
    return render(request, 'shop/BraceletAndRings.html')

def earrings(request):
    return render(request, 'shop/Earrings.html')

def necklace(request):
    return render(request, 'shop/necklace.html')

def cart_address(request):
    return render(request, 'shop/CartAddress.html')

def wishlist(request):
    return render(request, 'shop/MyWishlist.html')

def new_account(request):
    return render(request, 'shop/NewAccount.html')
