from rest_framework import serializers
from .models import items

class items_serializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = '__all__'