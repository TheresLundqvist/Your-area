from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NFLIvD76A0f0OXIjlU58D9Mb01jpxZDgZ6IIFsFCwSeCv8lo6I408op4li7EtCz5Q3IeIbKj0oeO4ulY7s5kLOB00iwAEowpJ',  # noqa
        'client_secret': 'sk_test_51NFLIvD76A0f0OXIfNNJs7Dd1vEeTZ2Qqnzle2GKgzCUMn1AVwog3AMN1n3KoYhtGJwKZIssa6YLOQNBeGHhVVAI008sbNOHws',  # noqa
    }

    return render(request, template, context)
