from rest_framework import serializers
from .models import Product
from decimal import Decimal


class ProductSerializer(serializers.ModelSerializer):
    price_with_discount = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'price_with_discount', 'created_at']


    def get_price_with_discount(self, obj):
        return obj.price * Decimal('0.85')
    

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value
