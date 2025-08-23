from django.contrib import admin
from django.urls import path, include
from core.views import CurrentUserView  

urlpatterns = [
    path("admin/", admin.site.urls),

    # Djoser endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # Custom endpoint for current user
    path('auth/users/me/', CurrentUserView.as_view(), name='current-user'),

    # Your product API
    path('api/products/', include('core.urls')),
]
