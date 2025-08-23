# Class based views vs function based views
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
from django.db.models import Count
import random
from rest_framework.generics import RetrieveAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

QUERY_ERROR_MESSAGE = 'No query provided'

class CategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class HomeCategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        queryset = models.Category.objects.all()
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:5]


class BrandList(generics.ListAPIView):
    serializer_class = serializers.BrandSerializer
    queryset = models.Brand.objects.all()


class ProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = models.Product.objects.all()
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:20]


class PopularProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = models.Product.objects.filter(ratings__gte=4.0, ratings__lte=5.0)
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:20]
    

class ProductListByClothesType(APIView):
    serializer_class = serializers.ProductSerializer

    def get(self, request):
        query = request.query_params.get('clothesType', None)

        if query:

            queryset = models.Product.objects.filter(clothesType=query)
            queryset = queryset.annotate(random_order=Count('id'))
            product_list = list(queryset)
            random.shuffle(product_list)

            limited_products = product_list[:20]

            serializer = serializers.ProductSerializer(limited_products, many=True)

            return Response(serializer.data)
        
        else:
            return Response({'message': QUERY_ERROR_MESSAGE}, status=status.HTTP_400_BAD_REQUEST)
        

class SimilarProducts(APIView):
    def get(self, request):
        query = request.query_params.get('category', None)

        if query:
            products = models.Product.filter(category=query)
            product_list = list(products)
            random.shuffle(product_list)
            limited_products = product_list[:6]
            serializer = serializers.ProductSerializer(limited_products, many=True)

            return Response(serializer.data)
        else:
            return Response({'message': QUERY_ERROR_MESSAGE}, status=status.HTTP_400_BAD_REQUEST)


class SearchProductByTitle(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)

        if query:
            products = models.Product.objects.filter(title_icontains=query)

            serializer = serializers.ProductSerializer(products)
            return Response(serializer.data)
        
        else:
            return Response({'message': QUERY_ERROR_MESSAGE}, status=status.HTTP_400_BAD_REQUEST)


class FilterProductByCategory(APIView):
    def get(self, request):
        query = request.query_params.get('category', None)

        if query:
            products = models.Product.objects.filter(category = query)
            serializer = serializers.ProductSerializer(products, many=True)
             
            return Response(serializer.data)
        else:
            return Response({'message': QUERY_ERROR_MESSAGE}, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(RetrieveAPIView):
            queryset = Product.objects.all()
            serializer_class = ProductSerializer
            lookup_field = 'pk' 
class ProductListCreateView(generics.ListCreateAPIView):
             queryset = Product.objects.all()
             serializer_class = ProductSerializer
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
                queryset = Product.objects.all()
                serializer_class = ProductSerializer
                lookup_field = 'pk'

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not user:
            return Response({'detail': 'User not found'}, status=404)
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'isAdmin': user.is_staff or user.is_superuser
        })