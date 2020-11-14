from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    message = None

    if item_id in list(bag.keys()):
        message = "This item already exists in your bag"
        bag[item_id] = quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    print(message)
    return redirect(redirect_url)