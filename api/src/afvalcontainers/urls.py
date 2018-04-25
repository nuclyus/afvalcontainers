"""Parkeervakken URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import routers
from rest_framework import permissions

from . import views as api_views


class ContainersView(routers.APIRootView):
    """
    Garbadge Containers in the city are show here as list.
    It is possible to filter the list
    """


class ContainerRouter(routers.DefaultRouter):
    APIRootView = ContainersView


containers = ContainerRouter()
containers.register(r"containers", api_views.ContainerView, base_name="container")
containers.register(r"wells", api_views.WellView, base_name="well")
containers.register(r"containertypes", api_views.TypeView, base_name="containertype")

urls = containers.urls

schema_view = get_schema_view(
   openapi.Info(
      title="Afval Container API",
      default_version='v1',
      description="Afvalcontainers en Wells in Amsterdam",
      terms_of_service="https://data.amsterdam.nl/",
      contact=openapi.Contact(email="datapunt@amsterdam.nl"),
      license=openapi.License(name="CC0 1.0 Universal"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^afval/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    url(r'^afval/swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    url(r'^afval/redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
    url(r"^afval/", include(urls)),
    url(r"^status/", include("afvalcontainers.health.urls")),
]
