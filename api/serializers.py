from rest_framework import serializers

from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "stock")

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be grater than 0.")
        return value
    

class ProductInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.DecimalField(max_digits=10, decimal_places=2)


class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product.name")
    price = serializers.DecimalField(
        source="product.price", max_digits=10, decimal_places=2
    )

    class Meta:
        model = OrderItem
        fields = (
            # 'order',
            "name",
            "price",
            "quantity",
            "item_subtotal",
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return sum(order_item.item_subtotal for order_item in obj.items.all())

    class Meta:
        model = Order
        fields = ("order_id", "user", "created", "status", "items", "total_price")
