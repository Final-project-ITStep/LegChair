from django.shortcuts import render


def index(request):
    return render(request, 'news/index.html', {
        'page_title': 'Новини',
        'page': 2
    })
