from django.shortcuts import render
from django.core.mail import send_mail
# https://docs.djangoproject.com/en/4.1/topics/email/
from cart.models import CardItem


def order(request, sel_list: str):
	str_list = sel_list.split(',')          # Exapmle -> '1,3,15450' => ['1', '3', '15450']
	num_list = [int(x) for x in str_list]   # ['1', '3', '15450'] => [1, 3, 15450]
	id_list = num_list[:-1]                 # [1, 3]
	total_price = num_list[-1]              # [15450]
	final_list = []
	for id_item in id_list:
		item = CardItem.objects.get(id=id_item)
		final_list.append({
			'product_name': item.product.name,
			'category_name': item.product.category.name,
			'product_price': item.product.price,
			'product_photo': item.product.photo
		})
	return render(request, 'orders/order.html', {
		'page_title': 'Деталі замовлення',
		'total_price': total_price,
		'final_list': final_list,
		'init_list': sel_list
	})


def confirm(request, init_list: str):
    if request.method == 'POST':
        email = request.POST['email']
        str_list = init_list.split(',')
        num_list = [int(x) for x in str_list]
        id_list = num_list[:-1]
        total_price = num_list[-1]
        info_list = []
        for id_item in id_list:
            item = CardItem.objects.get(id=id_item)
            info_list.append({
				'product_name': item.product.name,
				'category_name': item.product.category.name,
				'product_price': item.product.price,
			})
        subject = 'Повідомлення про замовлення на сайті LegChair'
        body = """
			<h1>Повідомлення про замовлення на сайті LegChair</h1>
			<hr />
			<h2>Ви підтвердили замовлення наступних товарів:</h2>
			<h3>
			<ol> """
        for item in info_list:
            body += f"""
				<li>
					{item.get('product_name')} / 
					{item.get('category_name')} - 
					{item.get('product_price')} грн.
				</li>"""
        body += f"""
			</ol>
			</h3>
			<hr />
			<h2>
				Загальна сума до сплати:
				<span>{total_price}</span>
			</h2> """
        if send_mail( subject, '', 'LegChair', [email], fail_silently=False, html_message=body ):
            return render(request, 'orders/thanks.html', {
				'page_title': 'Thank you',
				'email': email
			})
        else:
            return render(request, 'orders/failed.html', {
				'page_title': 'Send email failed',
				'email': email
			}) 
    return render(request, 'orders/confirm.html', {
        'page_title': 'Підтвердження замовлення',
        'init_list': init_list
    })