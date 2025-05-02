from django.db import models
from django.conf import settings
from django.db.models import Q

user = settings.AUTH_USER_MODEL
'''
    We create a method on the model queryset that return model with it 
    public being true
'''
class ProductQuerySet(models.QuerySet):
    def is_Public(self):
        return self.filter(public=True)
    # this search method help to filter the search futher down

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_Public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs |qs2).distinct()
        return qs

'''
the ideal is create our own custome quryset that inherite from the models.queryset
and we create a method that can filter base on the the field public is ture

    in a create model manager we overit the get_queryset mothod
    to return our custom created queryset so as to make use of the 
    our create method is_public
'''


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)
        # note the argument pass into the productqueryset is model and the database 
        # to be use

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)
    

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(user, default=1, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
    
    objects = ProductManager()

    @property
    def sale_price(self):
        return '%.2f' %(float(self.price)*0.8)

    def get_discount(self):
        return '123'

