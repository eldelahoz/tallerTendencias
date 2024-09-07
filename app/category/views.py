from rest_framework import viewsets
from .models import *
from .serializer import *

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer