from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def all_products(request):
    """ View to show individual product details """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")  # noqa
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa
            products = products.filter(queries)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View to show all products, including sorting and search queries """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
