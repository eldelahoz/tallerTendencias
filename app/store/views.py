from rest_framework import viewsets
from .models import *
from .serializer import *

class StoreViewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer