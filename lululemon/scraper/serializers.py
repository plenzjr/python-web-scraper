from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    """
    Serializer for product data
    """

    product_name = serializers.CharField(read_only=True)
    category = serializers.CharField(read_only=True)
    image = serializers.URLField(read_only=True)
    price = serializers.FloatField(read_only=True)
    currency = serializers.CharField(read_only=True)
    url = serializers.URLField(read_only=True)
