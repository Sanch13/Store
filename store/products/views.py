from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, "products/index.html", context=context)


def products(request):
    context = {
        'title': 'Store - catalog'
    }
    return render(request, "products/products.html", context=context)


def test_context(request):
    context = {
        "title": 'My first page',
        "header": 'You are welcome',
        "username": 'Aliaksandr Zubchyk',
        "products": [
            {"name": "Худи черного цвета с монограммами adidas Originals", "price": 6090.00},
            {"name": "Синяя куртка The North Face", "price": 23725.00},
            {"name": "Коричневый спортивный oversized-топ ASOS DESIGN", "price": 3390.00},
        ],
        "products_of_promotion": [
            {"name": "Черный рюкзак Nike Heritage", "price": 2340.00},
        ],
    }
    return render(request, "products/test_context.html", context=context)
