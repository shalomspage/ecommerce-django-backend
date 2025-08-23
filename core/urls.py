from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name="category-list"),
    path('categories/home/', views.HomeCategoryList.as_view(), name="home-category-list"),

     # Products CRUD
    path('', views.ProductListCreateView.as_view(), name="product-list-create"),
    path('<int:pk>/', views.ProductDetailView.as_view(), name="product-detail"),


    path('', views.ProductList.as_view(), name="product-list"),
    path('popular/', views.PopularProductList.as_view(), name="popular-list"),
    path('byType/', views.ProductListByClothesType.as_view(), name="list-by-type"),
    path('search/', views.SearchProductByTitle.as_view(), name="search"),
    path('category/', views.FilterProductByCategory.as_view(), name="products-by-category"),
    path('recommendations/', views.SimilarProducts.as_view(), name="-similar-products"),
    path('brands/', views.BrandList.as_view(), name="brand-list"),

    path('<int:pk>/', views.ProductDetail.as_view(), name="product-detail"),

    ]
