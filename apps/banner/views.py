from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from rest_framework import generics

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Banner

from .serializer import serializersBanner


class banner(viewsets.ModelViewSet, generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView,
             generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Banner.objects.all()
    serializer_class = serializersBanner
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['create_time', 'index']
    search_fields = ['index', ]