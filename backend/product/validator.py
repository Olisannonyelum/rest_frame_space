from .models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

def validate_title(value):
        qs = Product.objects.filter(title__exact=value)
        print('the value is ', value)
        if qs.exists():
            raise serializers.ValidationError(f'{value} this already a product name')
        return value

unique_product_title = UniqueValidator(queryset=Product.objects.all())