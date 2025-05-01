from django.urls import path

from .views import ( 
    ProductDetailAPIView,
    ProductListCreateAPIView,
    product_alt_view,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
    ProductMixinView
)


urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),#list
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view(), name='product_destroy'),
    # path('<int:pk>/', ProductMixinView.as_view()),#retrieve
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
   

    # path('', ProductMixinView.as_view())
    
]
# urlpatterns = [
#     path('<int:pk>/', product_alt_view),
#     path('', product_alt_view),
    
# ]

