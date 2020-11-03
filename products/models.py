from django.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural= 'Categories'
        
    name = models.CharField(max_length=254, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    lens = models.CharField(max_length=254, null=True, blank=True)
    resolution = models.CharField(max_length=254, null=True, blank=True)
    camera = models.CharField(max_length=254, null=True, blank=True)
    software = models.CharField(max_length=254, null=True, blank=True)
    aspectRatio = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    photographer = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name