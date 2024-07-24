
from django.urls import path
from .views import SKUListAPIView, SKUProductCountAPIView, UpdateProductInformationAPIView

urlpatterns = [

    path('sku-list/', SKUListAPIView.as_view(), name='sku-list-api'),
    path('<int:sku_id>/product-count', SKUProductCountAPIView.as_view(), name = 'sku-product-count'),
    path('<int:product_id>/', UpdateProductInformationAPIView.as_view(), name = 'update-product-id-info'),
]