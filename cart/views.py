from django.shortcuts import render
from django.http import JsonResponse
from .models import CardItem


def index(request):
	return render(request, 'cart/index.html', {
		'page_title': 'Управління Кошиком',
		'user_items': CardItem.objects.filter(user_id=request.user.id, cart_wish='add_cart'),
        'page': 1
	})

def wish(request):
	return render(request, 'cart/wish.html', {
		'page_title': 'Уподобання',
		'user_items': CardItem.objects.filter(user_id=request.user.id, cart_wish='add_wish'),
        'page': 1
	})


def ajax_cart_delete(request):
	CardItem.objects.get(id=request.GET['item']).delete()
	return JsonResponse({ 'report': 'Товар видалений' })


def ajax_wish_update(request):
	CardItem.objects.filter(id=request.GET['item']).update(cart_wish='add_cart')
	return JsonResponse({ 'report': 'Товар переміщений до Кошика' })


def select_all(uid) -> dict:
	user_items = CardItem.objects.filter(user_id=uid)
	amount_c, amount_w, count_c = 0.0, 0.0, 0
	for item in user_items:
		if item.cart_wish == 'add_cart':
			amount_c += item.product.price
			count_c += 1
		else:
			amount_w += item.product.price
	return {
		'count': [count_c, len(user_items) - count_c],
		'amount': [amount_c, amount_w]
	}


def ajax_cart(request):
	uid = request.GET['uid']

	# Add product
	CardItem.objects.create(
		user_id=uid,
		product_id=request.GET['pid'],
		cart_wish=request.GET['sid'],
		status='Очікування замовлення'
	)
	# Get back Count and Amount of products
	return JsonResponse(select_all(uid))


def ajax_cart_display(request):
	return JsonResponse(select_all(request.GET['uid']))

