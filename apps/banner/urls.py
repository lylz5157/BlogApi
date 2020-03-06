from django.conf.urls import url, include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'banner', views.banner, basename='banner')

urlpatterns = [
    url('', include(router.urls)),
]
