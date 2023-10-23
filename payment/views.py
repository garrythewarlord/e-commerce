from django.shortcuts import render, redirect
from .forms import fulfillForm

from purchase.models import CartItem, Cart
from .models import Order, OrderItem, PendingOrder
import uuid

from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse


def create_order(request):


	if not request.user.is_authenticated:
		return redirect('register')

	if request.method == 'POST':
		form = fulfillForm(request.POST)
		if form.is_valid():


			firstName = request.POST.get('firstName')
			secondName = request.POST.get('secondName')
			streethouseNumber = request.POST.get('streethouseNumber')
			city = request.POST.get('city')
			postal = request.POST.get('postal')		
			phone = request.POST.get('phone')

			#generate orderID
			orderID = str(uuid.uuid4())	

			user = request.user
			cart = Cart.objects.get(user=user)

			price = 0
			for item in cart.cartitem_set.all():
				price += float(item.product.price)
			
			price = str(price)

			order = Order.objects.create(user=user,
										 firstName=firstName,
										 secondName=secondName,
										 streethouseNumber=streethouseNumber,
										 city=city,
										 postal=postal,
										 phone=phone,
										 orderID=orderID,
										 price = price)

			for cart_item in cart.cartitem_set.all():
				order_item = OrderItem.objects.create(order=order, product=cart_item.product)
				order_item.save()


			cart.cartitem_set.all().delete()
			order.save()


		return redirect('view-order')

	return render(request, 'payment/submitOrder.html', {"form": fulfillForm()})



def orders_page(request):

	if not request.user.is_authenticated:
		return redirect('register')
			
	order =  Order.objects.filter(user=request.user)
	orderitems = OrderItem.objects.all()

	return render(request, 'payment/ordersPage.html', {'orders': order,
													   'orderitems': orderitems})



def remove_order(request):

	if not request.user.is_authenticated:
		return redirect('register')

	if request.method == 'POST':
		orderID = request.POST.get("remove_order")
		order=  Order.objects.filter(pk=orderID)
		order.delete()
		return redirect('view-order')




def checkout(request):

	if not request.user.is_authenticated:
		return redirect('register')

	host = request.get_host()

	order = request.POST.get("checkout")
	orderItems = OrderItem.objects.filter(order__orderID=order)

	totalPrice = 0
	for item in orderItems:
		totalPrice += float(item.product.price)
	totalPrice = format(totalPrice, '.2f')

	productNames = [item.product.title for item in orderItems]

	order = Order.objects.filter(orderID=order)[0]

	paypal_checkout = {
			'business': settings.PAYPAL_RECEIVER_EMAIL,
			'amount': totalPrice,
			'item_name': productNames,
			'invoice': order,
			'currency_code': 'EUR',
			'notify_url': f"http://{host}{reverse('paypal-ipn')}",
			'return_url': f"http://{host}{reverse('success', kwargs={'order_id': order})}",
			'cancel_url': f"http://{host}{reverse('failed', kwargs={'order_id': order})}"
	}


	paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

	context = {
		'orderrItems': orderItems,
		'paypal': paypal_payment,
	}

	return render(request, 'payment/checkout.html', context)		


def paymentsuccess(request, order_id):

	if not request.user.is_authenticated:
		return redirect('register')

	#set Order as paid
	order = Order.objects.filter(orderID=order_id).first()
	order.paid = True
	order.save()

	#create PendingOrders object
	order = Order.objects.filter(orderID=order_id).first()
	create_pending_order = PendingOrder.objects.create(order=order)
	create_pending_order.save()

	paid_orders = Order.objects.filter(paid=True)

	return render(request, 'payment/paymentsuccess.html', {'order': order_id})


def paymentfailed(request, order_id):

	if not request.user.is_authenticated:
		return redirect('register')

	return render(request, 'payment/paymentfailed.html', {'order': order_id})