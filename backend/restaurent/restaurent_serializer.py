from rest_framework import serializers
from .models import Category, Delivery, Notification, Order, OrderDetail, OrderWithFSM, Payment, Promotion, Restaurant, Menu, \
    MenuItem, Review, Contact
from rest_framework.serializers import ModelSerializer
from user_auth.user_serializer import UserListingSerializer

class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        return data
    

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        data['restaurant_name'] = instance.restaurant.name
        return data
    
class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        data['menu_name'] = instance.menu.name

        return data
    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['updated_at']


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        data['restaurant_name'] = instance.restaurant.name
        data['created_at_date'] = instance.created_at.date()
        data['order_details'] = OrderDetailSerializer(instance.order_detail_order.all(), many=True).data if instance.order_detail_order else None
        return data

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        data['order_bill'] = OrderSerializerList(instance.order).data if instance.order else None
        return data
    
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        data['restaurant_name'] = instance.restaurant.name if instance.restaurant else None
        return data
    

class PromotionSerializer(ModelSerializer):
    class Meta:
        model = Promotion
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        data['restaurant_name'] = instance.restaurant.name if instance.restaurant else None
        return data
    

class DeliverySerializer(ModelSerializer):
    class Meta:
        model = Delivery
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        data['order_bill'] = OrderSerializerList(instance.order).data if instance.order else None
        data['restaurant_name'] = instance.restaurant.name if instance.restaurant else None

        return data
    

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        return data
    

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        return data


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        data['restaurant_name'] = instance.restaurant.name

        return data

class OrderSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'bill']



class OrderWithFSMSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderWithFSM
        fields = ['id', 'bill', 'delivery_address', 'status', 'delivery_date', 'customer', 'restaurant', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']  # If you don't want these fields to be modified


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_by'] = UserListingSerializer(instance.created_by).data if instance.created_by else None
        data['updated_by'] = UserListingSerializer(instance.updated_by).data if instance.updated_by else None
        data['restaurant_name'] = instance.restaurant.name
        data['created_at_date'] = instance.created_at.date()
    
        return data

