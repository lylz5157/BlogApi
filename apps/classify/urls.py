from django.conf.urls import url, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'classify', views.classify, basename='classify')

urlpatterns = [
    url('', include(router.urls)),
]
