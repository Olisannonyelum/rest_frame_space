from rest_framework.reverse import reverse
from .models import Product
from rest_framework import serializers
from .validator import validate_title, unique_product_title
from api.PublicSerializer import UserPublicSerializer

class PublicInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    sale_price = serializers.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )    

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    '''
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    '''
    related_products = PublicInlineSerializer(source='user.product_set.all', many=True, read_only=True)
    user = UserPublicSerializer(read_only=True) #how dose this work?
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title, unique_product_title])
    name = serializers.CharField(source= 'pk', read_only=True)
    # username = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'related_products',
            # 'username',
            # 'edit_url', 
            # 'url',
            'name',
            'user',
            'pk',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    '''
    def get_username(self, obj):
        return {
            'user_data':obj.user.username
             }
    '''
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__exact=value)
    #     print('the value is ', value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} this already a product name')
    #     return value

    def create(self, validated_data):
        # email = validated_data.pop('email')
        obj =super().create(validated_data)
        # print(email, obj)
        return obj


    def get_url(self, obj):
        print(obj)
        request = self.context.get('request')
        print(request.POST)
        if request is None:
            return None
        # url = reverse(viewname='product_detail', kwargs={"pk":obj.pk}, request=request)
        print('this is the obj.........', obj, f'and this is the id and pk field{obj.pk}-{obj.id}')
        return reverse('product-detail', kwargs={"pk":obj.pk}, request=request)
        # return None


    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None

        if not isinstance(obj, Product):
            return None
          
        return obj.get_discount()
        
        print('start')