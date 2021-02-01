from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents

from checkout.models import Order

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@require_POST
@csrf_exempt
def stripe_webhooks(request):

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
        logger.info("Event constructed correctly")
    except ValueError:
        # Invalid payload
        logger.warning("Invalid Payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        logger.warning("Invalid signature")
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'charge.succeeded':
        # object has  payment_intent attr
        print('charge successssssssssssss')
        set_paid_until(event.data.object)

    return HttpResponse(status=200)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    payment_method = 'card'

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    customer_email = request.user.email

    stripe.api_key = stripe_secret_key
    payment_intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        payment_method_types=['card'],
    )

    context = {
        'client_secret': payment_intent.client_secret,
        'stripe_public_key': stripe_public_key,
        'customer_email': customer_email,
        'payment_intent_id': payment_intent.id,
        'order_form': order_form,
        'heading': 'checkout'

    }

    return render(request, 'checkout/checkout.html', context)


def card(request):
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    stripe_plan_id = request.POST['stripe_plan_id']
    automatic = request.POST['automatic']
    stripe.api_key = stripe_secret_key

    print('payment_intent_id')
    print(payment_intent_id)
    print('payment_method_id')
    print(payment_method_id)
    print('stripe_plan_id')
    print(stripe_plan_id)
    print('automatic')
    print(automatic)

    if automatic == 'Y':
        customer = stripe.Customer.create(
            email=request.user.email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )
        stripe.Subscription.create(
            customer=customer.id,
            items=[
                {
                    'plan': stripe_plan_id
                },
            ]
        )
        stripe.PaymentIntent.modify(
            payment_intent_id,
            payment_method=payment_method_id,
            customer=customer.id,
        )
    else:
        stripe.PaymentIntent.modify(
            payment_intent_id,
            payment_method=payment_method_id,
        )

    stripe.PaymentIntent.confirm(
        payment_intent_id
    )

    bag = request.session.get('bag', {})
    form_data = {
            'full_name': request.POST['full_name'],
            'email': request.user.email,
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'province_or_state': request.POST['province_or_state'],
        }
    order_form = OrderForm(form_data)
    print(form_data)
    if order_form.is_valid():
        order = order_form.save()
        for item_id, item_data in bag.items():
            try:
                product = Product.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=item_data,
                )
                order_line_item.save()
            except Product.DoesNotExist:
                messages.error(request, (
                    "One of the products in your bag wasn't found in our database. "
                    "Please call us for assistance!")
                )
                order.delete()
                return redirect(reverse('view_bag'))

        request.session['save_info'] = 'save-info' in request.POST
    else:
        messages.error(request, 'There was an error with your form. \
            Please double check your information.')


    return redirect(reverse('checkout_success', args=[order.order_number]))


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    from pprint import pprint
    pprint(request.body)
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    print(order)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_province_or_state': order.province_or_state,
                'default_email': request.user.email,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)