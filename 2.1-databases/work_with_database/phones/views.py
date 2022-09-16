from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    order = request.GET.get('sort')
    if order:
        if order == 'name':
            phones = [phone for phone in Phone.objects.order_by('name')]
        elif order == 'min_price':
            phones = [phone for phone in Phone.objects.order_by('price')]
        elif order == 'max_price':
            phones = [phone for phone in Phone.objects.order_by('-price')]
    else:
        phones = [phone for phone in Phone.objects.all()]
    template = 'catalog.html'
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = [p for p in Phone.objects.filter(slug=slug)]
    context = {
        'phone_search': phone,
    }
    return render(request, template, context)
