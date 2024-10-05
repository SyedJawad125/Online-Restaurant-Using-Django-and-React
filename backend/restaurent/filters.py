from django import forms
from django_filters import DateFilter, CharFilter, FilterSet, ChoiceFilter, BooleanFilter
from .models import *


class RestaurantFilter(FilterSet):
    id = CharFilter(field_name='id')
    # dept_updated_by_user= CharFilter(field_name='id')
    # dept_added_by_user= CharFilter(field_name='id')
    date_from = DateFilter(field_name='created_at', lookup_expr='gte' )
    date_to = DateFilter(field_name='created_at', lookup_expr='lte' )
    name = CharFilter(field_name='name', lookup_expr='icontains')
    # price = CharFilter(field_name='price')
    # description = CharFilter(field_name='description', lookup_expr='icontains')
    # rating = django_filters.RangeFilter()
    # opening_hours = django_filters.TimeFilter()
    # closing_hours = django_filters.TimeFilter()

    class Meta:
        model = Restaurant
        fields ='__all__'


class MenuFilter(FilterSet):
    id = CharFilter(field_name='id')
    date_from = DateFilter(field_name='created_at', lookup_expr='gte' )
    date_to = DateFilter(field_name='created_at', lookup_expr='lte' )
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Menu
        fields ='__all__'

class MenuItemFilter(FilterSet):
    id = CharFilter(field_name='id')
    date_from = DateFilter(field_name='created_at', lookup_expr='gte' )
    date_to = DateFilter(field_name='created_at', lookup_expr='lte' )
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = MenuItem
        # fields ='__all__'
        exclude = ['image']


class OrderFilter(FilterSet):
    id = CharFilter(field_name='id')
    # dept_updated_by_user= CharFilter(field_name='id')
    # dept_added_by_user= CharFilter(field_name='id')
    date_from = DateFilter(field_name='created_at', lookup_expr='gte' )
    date_to = DateFilter(field_name='created_at', lookup_expr='lte' )
    delivery_address = CharFilter(field_name='delivery_address', lookup_expr='icontains')
    bill = CharFilter(field_name='bill')

    class Meta:
        model = Order
        fields ='__all__'


class PaymentFilter(FilterSet):
    id = CharFilter(field_name='id')
    # dept_updated_by_user= CharFilter(field_name='id')
    # dept_added_by_user= CharFilter(field_name='id')
    date_from = DateFilter(field_name='created_at', lookup_expr='gte' )
    date_to = DateFilter(field_name='created_at', lookup_expr='lte' )
    start_date = DateFilter(field_name="transaction_date", lookup_expr='gte')
    end_date = DateFilter(field_name="transaction_date", lookup_expr='lte')
    # min_amount = django_filters.NumberFilter(field_name="amount", lookup_expr='gte')
    # max_amount = django_filters.NumberFilter(field_name="amount", lookup_expr='lte') ok karny hain.
    

    class Meta:
        model = Payment
        fields ='__all__'

class ReviewFilter(FilterSet):
    id = CharFilter(field_name='id')
    min_rating = forms.IntegerField(min_value=0, max_value=5, required=False)
    max_rating = forms.IntegerField(min_value=0, max_value=5, required=False)
    start_date = DateFilter(field_name="transaction_date", lookup_expr='gte')
    end_date = DateFilter(field_name="transaction_date", lookup_expr='lte')
    restaurant_name = forms.CharField(max_length=200, required=False)
    # start_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    # end_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))


    class Meta:
        model = Review
        fields ='__all__'



class PromotionFilter(FilterSet):
    id = CharFilter(field_name='id')
    start_date = DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = DateFilter(field_name='end_date', lookup_expr='lte')
    # discount_percentage = django_filters.RangeFilter()
    # active = django_filters.BooleanFilter()
    # promo_code = django_filters.CharFilter(field_name='promo_code', lookup_expr='icontains')

    class Meta:
        model = Promotion
        fields = ['start_date', 'end_date', 'discount_percentage', 'active', 'promo_code']


class DeliveryFilter(FilterSet):
    id = CharFilter(field_name='id')
    date_from = DateFilter(field_name='created_at', lookup_expr='gte' )
    date_to = DateFilter(field_name='created_at', lookup_expr='lte' )
    customer_name = CharFilter(field_name='customer_name', lookup_expr='icontains')
    delivery_person_name = CharFilter(field_name='delivery_person_name', lookup_expr='icontains')
    restaurant_name = CharFilter(field_name='restaurant_name', lookup_expr='icontains')
    total_amount = CharFilter(field_name='total_amount')


    class Meta:
        model = Delivery
        fields ='__all__'


class NotificationFilter(FilterSet):
    id = CharFilter(field_name='id')
    notification_type = ChoiceFilter(choices=Notification.NOTIFICATION_TYPE_CHOICES)
    read = BooleanFilter(field_name='read')
    # created_at = DateFromToRangeFilter()

    class Meta:
        model = Notification
        fields = ['notification_type', 'read']


class CategoryFilter(FilterSet):
    id = CharFilter(field_name='id')
    date_from = DateFilter(field_name='created_at', lookup_expr='gte' )
    date_to = DateFilter(field_name='created_at', lookup_expr='lte' )
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Category
        fields ='__all__'


class ContactFilter(FilterSet):
    id = CharFilter(field_name='id')
    date_from = DateFilter(field_name='created_at', lookup_expr='gte' )
    date_to = DateFilter(field_name='created_at', lookup_expr='lte' )
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Contact
        fields ='__all__'


class OrderWithFSMFilter(FilterSet):
    id = CharFilter(field_name='id')
    # dept_updated_by_user= CharFilter(field_name='id')
    # dept_added_by_user= CharFilter(field_name='id')
    date_from = DateFilter(field_name='created_at', lookup_expr='gte' )
    date_to = DateFilter(field_name='created_at', lookup_expr='lte' )
    delivery_address = CharFilter(field_name='delivery_address', lookup_expr='icontains')
    bill = CharFilter(field_name='bill')

    class Meta:
        model = OrderWithFSM
        fields ='__all__'
