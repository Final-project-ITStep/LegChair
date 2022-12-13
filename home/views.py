from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    return render(request, 'home/index.html', {
        'page_title': 'Головна',
        'page': 0
    })


def contact(request):
    if request.method == 'GET':
        return render(request, 'home/contact.html', {
            'page_title': 'Контакти',
            'result': '',
            'page': 3
        })
    elif request.method == 'POST':
        body = f"""
        <strong>   From: </strong>{request.POST['name']}<span></span><br/>
        <strong>Subject: </strong>{request.POST['subject']}<span></span><br/><hr/> 
        <strong>Message: </strong>{request.POST['message']}<span></span> """
        success = send_mail('Customer message', '', 'customer@onlineshop.ua',
                            [request.POST['email']], fail_silently=False, html_message=body)
        return render(request, 'home/contact.html', {
            'page_title': 'Контакти',
            'result': True if success else False,
            'page': 3
        })

def blog(request):
    return render(request, 'home/blog.html', {
        'page_title': 'Новини',
        'page': 0
    })
