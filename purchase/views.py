from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required
from .models import CartItem, Cart
from home.models import Products
from django.http import HttpResponse


from .forms import fulfillForm

#@login_required
def dashboard(request):

	#redirect customer to register before purchasing
	if not request.user.is_authenticated:
		return redirect('register')

	#Creats a Cart and CartItem objects for signed user and displays it
	if request.method == 'POST':
		product_ID = request.POST.get('product_id')
		product = get_object_or_404(Products, pk=product_ID)
		cart, created = Cart.objects.get_or_create(user=request.user)	
		cart_item = CartItem.objects.create(cart=cart, product=product)
		cart_item.save()
		product.quantity = str(int(product.quantity) - 1)
		product.save()

	cart = CartItem.objects.filter(cart__user=request.user.id)
	total_price = 0
	count = cart.count

	for prod in cart:
		test = float(prod.product.price.replace("€", ''))
		total_price += test

	data = {
		'cart_items': CartItem.objects.filter(cart__user=request.user),
		'count': count,
		'total_price': str(total_price)
	}
	
	return render(request, 'purchase/basket.html',data)


def remove_basket(request):

	if not request.user.is_authenticated:
		return redirect('register')
	
	#remove product from the cartItem object
	if request.method == 'POST':
		orderitem = request.POST.get('remove_product')
		cart_item = CartItem.objects.filter(pk=orderitem)[0]
		update_quantity = CartItem.objects.filter(pk=orderitem)[0].product
		update_quantity.quantity = str(int(update_quantity.quantity)+1)
		update_quantity.save()
		cart_item.delete()

		return redirect('dashboard')



