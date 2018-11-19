"""django_bootstrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.views.generic import RedirectView

from rest_framework import (routers, permissions)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from apps.home.utils import generate_url
from apps.home.views import CheckmarksViewSet

router = routers.DefaultRouter()

schema_view_yasg = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='v1',
      description="Test backend",
      terms_of_service="",
      contact=openapi.Contact(email="contact@codebnb.me"),
      license=openapi.License(name=""),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    generate_url(r'swagger/$', schema_view_yasg.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    url(r'^$', RedirectView.as_view(url=settings.API_VERSION_URL)),
    url(r'^home', include('apps.home.urls', namespace='home')),
]

router = routers.DefaultRouter()
router.register(r'checkmarks', CheckmarksViewSet, base_name='checkmarks')
urlpatterns.append(generate_url('', include(router.urls)))
