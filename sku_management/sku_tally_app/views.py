from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SKU, Product
from .serializers import SKUSerializer, ProductSerializer
from django.shortcuts import get_object_or_404

class SKUListAPIView(APIView):
    def get(self, request):
        skus = SKU.objects.all()
        serializer = SKUSerializer(skus, many=True)
        return Response(serializer.data)

class SKUProductCountAPIView(APIView):
    def get(self, request, sku_id):
        sku = get_object_or_404(SKU, id=sku_id)
        product_count = sku.products.count()
        return Response({'product_count': product_count})

class UpdateProductInformationAPIView(APIView):
    def post(self, request, product_id):
        product = Product.objects.filter(id=product_id).first()
        if product:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)