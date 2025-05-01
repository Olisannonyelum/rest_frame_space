from django.http import JsonResponse, HttpResponse
import json #this library is use to convert json data into python dic
from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    
    serializerInstance= ProductSerializer(data=request.data)
    # print('............>', type(request.data),
    # 'this is the data', request.data
    # )
    if serializerInstance.is_valid(raise_exception=True):
        
        # productinstance = serializerInstance.save()
        data = serializerInstance.data
        print(serializerInstance.data)
        return Response(data)
    return Response({'invalide':'not good data'}, status=400)

# Create your views here.

