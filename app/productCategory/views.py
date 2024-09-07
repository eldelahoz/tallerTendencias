from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filter.rest_framework import DjangoFilterBackend
from .models import *
from .serealizer import *

class productCategoryViewset(viewsets.ModelViewSet):
    queryset = product_category.objects(all)
    serializer_class = productCategorySerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')




