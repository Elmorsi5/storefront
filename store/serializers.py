from rest_framework import serializers
from .models import Product, Collection, Promotion
from decimal import Decimal


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "price", "price_with_tax", "collection"]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(), view_name="collection-detail"
    )

    def calculate_tax(self, product: Product):
        return product.price * Decimal(1.1)