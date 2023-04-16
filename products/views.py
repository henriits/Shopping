from django.shortcuts import render


# Create your views here.
def home(requests):
    context = {
        'cart_entries': [
            {
                'title': 'GOOD SHOES!',
                'body': 'I have created my first template in Django!',

            },
            {
                'title': 'QUALITY ITEMS',
                'body': 'Something else in there',

            },
            {
                'title': 'SOMETHING ELSE!!',
                'body': 'Am i doing it right?',

            },
            {
                'title': 'NEW!!',
                'body': 'Am i doing it right?',

            },
            {
                'title': 'DISCOUNTED',
                'body': 'Am i doing it right?',

            }
        ]
    }

    return render(requests, 'home.html', context)


def products(requests):
    return render(requests, "products.html")
