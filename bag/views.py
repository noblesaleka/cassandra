from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product
from django.conf import settings
from bag.contexts import bag_contents
import stripe

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    
    heading = "Shopping Bag"
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
    amount=stripe_total,
    currency=settings.STRIPE_CURRENCY,
    payment_method_types = ['card'],
    )
    print('------------------BAG this is payment intent ' + str(intent.id))
    payment_intent_id = intent.id
    secret_key = intent.client_secret
    print('------------------BAG this is secret key' + str(secret_key))

    if request.user.is_authenticated:
        customer_email = request.user.email
    else:
        customer_email = 'no email'


    print (customer_email)
    
    context = {
        'heading': heading,
        'payment_intent_id':intent.id,
        'stripe_public_key': stripe_public_key,
        'customer_email':customer_email,
        'payment_intent_id': payment_intent_id,
        'secret_key': secret_key,
        
    }

    return render(request, 'bag/bag.html', context)

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    message = None

    if item_id in list(bag.keys()):
        bag[item_id] = quantity
        messages.success(request, f'{product.name} already exists in your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    print(message)
    return redirect(redirect_url)



def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} to your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
            messages.error(request, f'Error removing item: {e}')
            return HttpResponse(status=500)