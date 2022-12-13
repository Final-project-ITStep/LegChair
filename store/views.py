from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Producer, Product, Color


def index(request):
    all_products = Product.objects.all()
    page_size = 6
    paginator = Paginator(all_products, page_size)
    page_number = request.GET.get('page')

    return render(request, 'store/index.html', {
        'page_title': 'Каталог товарів',
        'all_products': all_products,
        'all_categories': Category.objects.all(),
        'all_producers': Producer.objects.all(),
        'all_colors': Color.objects.all(),
        'paginate_products': paginator.get_page(page_number),
        'page': 1
    })

def single_product(request, product_id: int):
    return render(request, 'store/single.html', {
        'page_title': 'Опис товару',
        'product_id': Product.objects.get(product_id=id)
    })