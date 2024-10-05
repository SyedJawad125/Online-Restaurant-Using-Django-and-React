from datetime import timezone
from django.db import models
from user_auth.models import User

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    opening_hours = models.CharField(max_length=100)
    closing_hours = models.CharField(max_length=100)
    cuisine_type = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='restaurent_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurent_updated_by', null=True, blank=True)
    

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE ,related_name='restaurent1',null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='menu_created_by',null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='menu_updated_by',null=True, blank=True)


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # category = models.ForeignKey(MenuCategory, related_name='menu_items', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    image = models.FileField(upload_to='menu_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    menu= models.ForeignKey(Menu, on_delete=models.CASCADE ,related_name='menu1',null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='menuitem_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='menuitem_updated_by', null=True, blank=True)


class Order(models.Model):
    status_choices = (
            ("booked", "booked"),
            ("in_process", "in_process"),
            ("delivered", "delivered")
        )
    bill = models.PositiveBigIntegerField(null=True, blank=True)
    delivery_address = models.TextField()
    status = models.CharField(max_length=50, choices = status_choices, null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    # rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_rider', null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='order_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_updated_by', null=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_customer', null=True,blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_order', null=True,blank=True)



class OrderDetail(models.Model):
    unit_price = models.PositiveBigIntegerField()
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveBigIntegerField()
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_detail_product')
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='menuitem_detail',null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_detail_order', null=True, blank=True)
    


class Payment(models.Model):
    
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Mobile Payment', 'Mobile Payment'),
    ]
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount paid")
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default='Cash',)
    transaction_date = models.DateTimeField(auto_now_add=True)
    card_number = models.CharField(max_length=16, blank=True, null=True, help_text="Credit/Debit card number if applicable")
    card_holder_name = models.CharField(max_length=100, blank=True, null=True, help_text="Name of the cardholder if applicable")
    # mobile_payment_id = models.CharField(max_length=100, blank=True, null=True, help_text="Mobile payment transaction ID if applicable")
    is_successful = models.BooleanField(default=True, help_text="Status of the payment")
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='payment_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_updated_by', null=True, blank=True)



class Review(models.Model):

    rating = models.PositiveSmallIntegerField()  # Assuming rating is from 1 to 5
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='review_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_updated_by', null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_reviews', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_can_reviews', null=True, blank=True)



class Promotion(models.Model):
    name = models.CharField(max_length=100)  # Name of the promotion
    description = models.TextField(blank=True, null=True)  # Description of the promotion
    start_date = models.DateField()  # Start date of the promotion
    end_date = models.DateField()  # End date of the promotion
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Discount percentage
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Discount amount
    active = models.BooleanField(default=True)  # Whether the promotion is active or not
    promo_code = models.CharField(max_length=50, blank=True, null=True)  # Optional promo code for the promotion
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_promotions', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='promotion_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='promotion_updated_by', null=True, blank=True)


class Delivery(models.Model):
    
    customer_name = models.CharField(max_length=200)
    customer_address = models.TextField()
    customer_phone = models.CharField(max_length=15)
    delivery_status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending') , ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered') , ('Cancelled', 'Cancelled')
    ])
    delivery_date = models.DateField(null=True, blank=True)
    delivery_person_name = models.CharField(max_length=200, blank=True, null=True)
    delivery_person_contact = models.CharField(max_length=15, blank=True, null=True)
    restaurant_address = models.TextField()
    restaurant_phone = models.CharField(max_length=15)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Paid', 'Paid')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_delivery', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='delivery_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery_updated_by', null=True, blank=True)


class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ('order', 'Order'),
        ('reservation', 'Reservation'),
        ('promotion', 'Promotion'),
        ('reminder', 'Reminder'),
    ]

    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_notification', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_notification', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='notification_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_updated_by', null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='category_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_updated_by', null=True, blank=True)



class MenuItemCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='menuitemcategory_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='menuitemcategory_updated_by', null=True, blank=True)


# class MenuItemCategory(models.Model):
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, db_column='MenuItemID')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='CategoryID')

#     class Meta:
#         unique_together = (('menu_item', 'category'),)
#         verbose_name = "Menu Item Category"
#         verbose_name_plural = "Menu Item Categories"

class Contact(models.Model):

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='contacts', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_created_by',
                                   null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_updated_by',
                                   null=True, blank=True)
    


from django_fsm import FSMField, transition
from django.db import models


class OrderWithFSM(models.Model):
    status_choices = (
        ("booked", "booked"),
        ("in_process", "in_process"),
        ("delivered", "delivered")
    )

    bill = models.PositiveBigIntegerField(null=True, blank=True)
    delivery_address = models.TextField()
    status = FSMField(default="booked", choices=status_choices)  # Using FSMField for status
    delivery_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderwithfsm_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderwithfsm_updated_by', null=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderwithfsm_customer', null=True, blank=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name='restaurantwithfsm_order', null=True, blank=True)

    # FSM Transitions
    @transition(field=status, source='booked', target='in_process')
    def process_order(self):
        """ Transition from 'booked' to 'in_process'. """
        pass

    @transition(field=status, source='in_process', target='delivered')
    def deliver_order(self):
        """ Transition from 'in_process' to 'delivered'. """
        pass

    @transition(field=status, source=['booked', 'in_process'], target='booked')
    def reset_order(self):
        """ Transition back to 'booked'. """
        pass