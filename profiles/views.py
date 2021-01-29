import logging
import stripe
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import UserProfile
from .forms import UserProfileForm
from products.models import Product
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def membership(request):
    products = Product.objects.all()
    products = products.filter(category__name__icontains='membership')

    request_user = request.user

    context = {
        'products': products,
    }
    return render(request, 'profiles/membership.html', context)

def set_paid_until(charge):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    pi = stripe.PaymentIntent.retrieve(charge.payment_intent)
    subscription_id = charge.subscription
    print('this is subscription id ' + subscription_id)

    if pi.customer:
        customer = stripe.Customer.retrieve(pi.customer)
        email = customer.email
        if customer:
            subscr = stripe.Subscription.retrieve(
                    subscription_id
                )
        
            current_period_end = subscr['current_period_end']
            print(current_period_end)

        try:
            user = UserProfile.objects.get(default_email=email)
        except UserProfile.DoesNotExist:
            print(
                f"User with email {email} not found"
            )
            return False

        user.set_paid_until(current_period_end)
        print(f"Profile with {current_period_end} saved for user {email}")
    
         
    else:
        pass