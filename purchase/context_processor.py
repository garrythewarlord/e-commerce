#Context Processor is a python function(s) that displays a single or multiple pieces of information across every tempalte rendered in my project

from purchase.models import CartItem

def basketCount(request):
	count = CartItem.objects.filter(cart__user=request.user.id).count
	return {"count": count}
