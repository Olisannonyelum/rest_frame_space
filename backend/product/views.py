from rest_framework import generics, mixins, permissions, authentication 
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .permissions import IsStaffEditorPermission
from api.mixins import IsStaffEditorPermission, UserQuerySetMixin


# the below is a generic base views


class ProductDetailAPIView(
    generics.RetrieveAPIView, 
    IsStaffEditorPermission
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

'''
    there is something i notice from the arrangement of this inherited class
    when i inherite userQuerysetmixin last the get_queryset did not applie 
    but when i inherite from it first it applied  
'''
class ProductListCreateAPIView(
    UserQuerySetMixin,
    generics.ListCreateAPIView, 
    IsStaffEditorPermission,
    ):
    # allow_staff_view = False 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        email = serializer.validated_data.pop('email')
        serializer.save(user=self.request.user)
        # super().perform_create(serializer)
    '''
    i inherite from the custom missing so this  method is no longer neccessary 

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        user = self.request.user

        return qs.filter(user=user)
    '''
'''
    in the updata api is much different from the other's
    it contain additional field which is the lookup_field, that is from the url
    http:://localhost:8000/api/product/<int:pk>/update/' 
    and it contain function that is only called by the update api

    and  lastly and to be noted this api make use of the request method PUT
    and it inherite from generic.updateapiview
'''

class ProductUpdateAPIView(
    generics.UpdateAPIView, 
    IsStaffEditorPermission
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        '''
            this is where we perform our modification, that is that 'request.data'
            that is pass in behind the scence of this class which we can not see put
            it sent behind the backend of the class 
        '''
        instance = serializer.save()
        if instance.content is None:
            instance.content = instance.title


class ProductDestroyAPIView(
    generics.DestroyAPIView,
    IsStaffEditorPermission
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    '''
        the destroy api looking similier to the update the request methode it allow is the delete 
        and NOTE this view dose'nt return any json data if you are aspecting one on the client side 
        the might flag an error 
    '''
    def perform_destroy(self, instance):
        data = ProductSerializer(instance).data
        print(f'the instance\n{data}\n....is delete')
        
        super().perform_destroy(instance)



# the below is a function base view

'''
this below is a view that can handle but create, list and detail. 
it show how the generic view that is the listcreateapiview work



'''

@api_view(['POST', 'GET'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
        
    if method == 'GET':
        # detail view
        if pk is not None:
            instance = get_object_or_404(Product, id=pk)            
            data =ProductSerializer(instance).data
            return Response(data)
        # list view
        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)

    if method == 'POST':
        # create views
        # InData = request.data
        serialized = ProductSerializer(data=request.data)
        if serialized.is_valid(raise_exception=True):
            serialized.save( content = 'it is save')
            data = serialized.data
            return Response(data)
        return Response({'massage':'unserializable'}, status=404)




'''
    working with the core class generic and mixinin 
    to see how this previous class work

'''
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView,
    ):
    '''
        the mixins provide us to  assign the attribut queryset and so, for more attribut consulte the documentation
        then the genericsapiview enable us to make us of the method to indicate which
        to call base on the request.method type,
        and the self.list()is coming from the mixin, with this this is the simple display of how the 
        Generic.ListAPIView is implimented, because it inherite from the core class genericapiview and  mixins.listmodelmixin,
        so what am saying is that this is a listapiview in the flesh
    '''

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(kwargs)
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        print('this sheet is runing.....')
        super().perform_create(serializer)