from django.views.generic import ListView
from products.models import Product


class Home(ListView):
    model = Product
    template_name = 'home/index.html'
    context_object_name = 'products'


# def index(request):
#     products = Product.objects.all()

#     context = {
#         'products': products,
#     }
#     return render(request, 'home/index.html', context)
