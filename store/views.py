from django.shortcuts import render, redirect
from .models import Product

def index(request):
    # 抓取所有商品
    items = Product.objects.all()
    
    # 從 Session 抓取購物車內容，如果沒有就給空的
    cart = request.session.get('cart', {})
    
    # 計算購物車內的商品總數與總金額
    cart_items = []
    total_price = 0
    total_count = 0
    
    for p_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=p_id)
            subtotal = product.price * quantity
            total_price += subtotal
            total_count += quantity
            cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
        except Product.DoesNotExist:
            continue

    return render(request, 'index.html', {
        'items': items,
        'cart_items': cart_items,
        'total_price': total_price,
        'total_count': total_count,
    })

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    p_id_str = str(product_id)
    cart[p_id_str] = cart.get(p_id_str, 0) + 1
    request.session['cart'] = cart
    return redirect('/')

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('/')