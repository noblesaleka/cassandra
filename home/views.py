from django.views.generic import ListView
from products.models import Product


class Home(ListView):
    model = Product
    template_name = 'home/index.html'
    context_object_name = 'products'

