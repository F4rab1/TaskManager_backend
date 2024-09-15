"""
URL configuration for TaskManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'register', UserViewSet, basename='user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('task.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api/', include(router.urls)),  # Custom API registration route
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('djoser.urls')), 
    path('auth/', include('djoser.urls.jwt')), 
]

