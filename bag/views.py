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
       
    context = {
        'heading': heading,
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