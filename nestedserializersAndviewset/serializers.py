from rest_framework import serializers
from .models import Brand, Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id', 'name', 'description', 'price', 'brand']


class BrandSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True, read_only=True)
    class Meta:
        model = Brand
        fields = ['id', 'name', 'phones']
