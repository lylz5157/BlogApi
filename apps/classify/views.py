from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from rest_framework import filters

from rest_framework import generics

from .models import db_classify

from .serializer import db_classifyserializers


class classify(viewsets.ModelViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView,
               generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = db_classify.objects.all()
    serializer_class = db_classifyserializers
