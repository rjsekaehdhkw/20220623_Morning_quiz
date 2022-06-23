from rest_framework import serializers

from item.models import Category as CategoryModel
from item.models import Item as ItemModel
from item.models import Order as OrderModel
from item.models import ItemOrder as ItemOrderModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = "CategoryModel"
        field = ["name"]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = "ItemModel"
        field = ["name", "image_url", "category_id"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = "OrderModel"
        field = ["delivery_address", "order_date"]


class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = "ItemOrderModel"
        field = ["item_count", "item_id", "order_id"]
