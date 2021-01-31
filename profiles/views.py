import logging
import stripe
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile
from .forms import UserProfileForm
from products.models import Product
from checkout.models import Order


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = get_object_or_404(UserProfile, user=request.user)
        context = {
            'form': UserProfileForm(instance=profile),
            'orders': profile.orders.all(),
            'on_profile_page': True,
        }
        return render(request, 'profiles/profile.html', context)

    def post(self, request):
        profile = get_object_or_404(UserProfile, user=request.user)
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
        return redirect('profile')

class OrderHistoryView(LoginRequiredMixin, View):
    def get(self, request, order_number):
        order = get_object_or_404(Order, order_number=order_number)
        help_text = f'This is a past confirmation for order number {order_number}.'
        feedback = 'A confirmation email was sent on the order date.'
        message = f'{help_text} {feedback}'
        messages.info(request, message)
        context = {
            'order': order,
            'from_profile': True,
        }
        return render(request, 'checkout/checkout_success.html', context)



class MembershipView(ListView):
    model = Product
    template_name = 'profiles/membership.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category__name__icontains='membership')
        return context


    

def membership(request):
    products = Product.objects.filter(category__name__icontains='membership')
    context = {'products': products,    }
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