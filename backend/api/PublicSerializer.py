from rest_framework import serializers

class UserPublicInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    sale_price = serializers.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )    

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        print(obj)
        user = obj
        my_products_qs = user.product_set.all().first()
        related_data = UserPublicInlineSerializer(my_products_qs, context=self.context
        ).data
        return related_data




    
    