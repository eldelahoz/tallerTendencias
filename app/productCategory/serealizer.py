from rest_framework import serializer
from .models import *

class productCategorySerializer(serializer.ModelSerializer):

    class meta:
        model = product_category
        fields = ('__all__')