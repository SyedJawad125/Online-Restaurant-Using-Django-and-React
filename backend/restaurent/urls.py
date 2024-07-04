from django.urls import path
from .views import ContactViews, CategoryViews, DeliveryViews, MenuItemViews, MenuViews, NotificationViews, PaymentViews, PromotionViews, RestaurantViews, OrderViews, ReviewViews

urlpatterns = [
    path('restaurant', RestaurantViews.as_view({"get": "get_restaurant",
                                                "post": "post_restaurant",
                                                "patch": "update_restaurant",
                                                "delete": "delete_restaurant"})),

    path('menu', MenuViews.as_view({"get": "get_menu",
                                                "post": "post_menu",
                                                "patch": "update_menu",
                                                "delete": "delete_menu"})),
    path('menuitem', MenuItemViews.as_view({"get": "get_menuitem",
                                                "post": "post_menuitem",
                                                "patch": "update_menuitem",
                                                "delete": "delete_menuitem"})),
                                                
    path('order', OrderViews.as_view({"get": "get_order",
                                                "post": "post_order",
                                                "patch": "update_order",
                                                "delete": "delete_order"})),

    path('payment', PaymentViews.as_view({"get": "get_payment",
                                                "post": "post_payment",
                                                "patch": "update_payment",
                                                "delete": "delete_payment"})),

    path('review', ReviewViews.as_view({"get": "get_review",
                                                "post": "post_review",
                                                "patch": "update_review",
                                                "delete": "delete_review"})),


    path('promotion', PromotionViews.as_view({"get": "get_promotion",
                                                "post": "post_promotion",
                                                "patch": "update_promotion",
                                                "delete": "delete_promotion"})),


    path('delivery', DeliveryViews.as_view({"get": "get_delivery",
                                                "post": "post_delivery",
                                                "patch": "update_delivery",
                                                "delete": "delete_delivery"})),

                                        
    path('notification', NotificationViews.as_view({"get": "get_notification",
                                                "post": "post_notification",
                                                "patch": "update_notification",
                                                "delete": "delete_notification"})),

                
    path('category', CategoryViews.as_view({"get": "get_category",
                                                "post": "post_category",
                                                "patch": "update_category",
                                                "delete": "delete_category"})),

    path('contact', ContactViews.as_view({"get": "get_contact",
                                                "post": "post_contact",
                                                "patch": "update_contact",
                                                "delete": "delete_contact"})),
   
]