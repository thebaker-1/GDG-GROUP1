
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
  openapi.Info(
    title="social media app API",
    default_version='1.0.0',
    description="API documentation of App",
  ),
  public=True,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         include([
           path('api/', include('users.urls')),
           path('api/', include('posts.urls')),
           path('api/', include('interactions.urls')),
           path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
         ])
         )
]
