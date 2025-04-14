"""
URL configuration for social_media_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework import permissions
from drf_yasg.views import get_schema_view as view
from drf_yasg import openapi

    
# API schema view setup for a social media app
schema_view = view(
   openapi.Info(
      title="Social Media API",
      default_version='v1',
      description="API documentation for the Social Media App. This API allows user management, posts, comments, and interactions.",
      contact=openapi.Contact(email="aschalewgetahun238@gmail.com"),  
      license=openapi.License(name="MIT License"),  
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),  # Public access for API docs
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         include([
           path('api/', include('users.urls')),
           path('api/', include('posts.urls')),
           path('api/', include('interactions.urls')),
           path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
           path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
           path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
         ])
         )
]