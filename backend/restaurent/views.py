from django.shortcuts import render
from . models import Restaurant
from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from utils.base_authentication import JWTAuthentication
from .restaurent_controller import  CategoryController, ContactController, DeliveryController, MenuController, MenuItemController, NotificationController, OrderController, OrderWithFSMController, PaymentController, PromotionController, RestaurantController, ReviewController
from permissions.decorator import permission_required
# Create your views here.


restaurant_controller = RestaurantController()
menu_controller = MenuController()
menuitem_controller = MenuItemController()
order_controller = OrderController()
payment_controller = PaymentController()
review_controller = ReviewController()
promotion_controller = PromotionController()
delivery_controller = DeliveryController()
notification_controller = NotificationController()
category_controller = CategoryController()
contact_controller = ContactController()
orderwithfsm_controller = OrderWithFSMController()



class RestaurantViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    # @permission_required(['create_restaurant'])
    def post_restaurant(self, request):
        return restaurant_controller.create(request)
    # @permission_required(['get_restaurant'])
    def get_restaurant(self, request):
        return restaurant_controller.get_restaurant(request)
    
    # @permission_required(['update_restaurant'])
    def update_restaurant(self, request):
        return restaurant_controller.update_restaurant(request)
    
    # @permission_required(['delete_restaurant'])
    def delete_restaurant(self, request):
        return restaurant_controller.delete_restaurant(request)
    

class MenuViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    # @permission_required(['create_restaurant'])
    def post_menu(self, request):
        return menu_controller.create(request)
    # @permission_required(['get_restaurant'])
    def get_menu(self, request):
        return menu_controller.get_menu(request)
    
    # @permission_required(['update_restaurant'])
    def update_menu(self, request):
        return menu_controller.update_menu(request)
    
    # @permission_required(['delete_restaurant'])
    def delete_menu(self, request):
        return menu_controller.delete_menu(request)
    

class MenuItemViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    # @permission_required(['create_restaurant'])
    def post_menuitem(self, request):
        return menuitem_controller.create(request)
    # @permission_required(['get_restaurant'])
    def get_menuitem(self, request):
        return menuitem_controller.get_menuitem(request)
    
    # @permission_required(['update_restaurant'])
    def update_menuitem(self, request):
        return menuitem_controller.update_menuitem(request)
    
    # @permission_required(['delete_restaurant'])
    def delete_menuitem(self, request):
        return menuitem_controller.delete_menuitem(request)
    

class OrderViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_order(self, request):
        return order_controller.create(request)

    def get_order(self, request):
        return order_controller.get_order(request)

    def update_order(self, request):
        return order_controller.update_order(request)

    def delete_order(self, request):
        return order_controller.delete_order(request)
    

class PaymentViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_payment(self, request):
        return payment_controller.create(request)

    def get_payment(self, request):
        return payment_controller.get_payment(request)

    def update_payment(self, request):
        return payment_controller.update_payment(request)

    def delete_payment(self, request):
        return payment_controller.delete_payment(request)
    

class ReviewViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_review(self, request):
        return review_controller.create(request)

    def get_review(self, request):
        return review_controller.get_review(request)

    def update_review(self, request):
        return review_controller.update_review(request)

    def delete_review(self, request):
        return review_controller.delete_review(request)
    

class PromotionViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_promotion(self, request):
        return promotion_controller.create(request)

    def get_promotion(self, request):
        return promotion_controller.get_promotion(request)

    def update_promotion(self, request):
        return promotion_controller.update_promotion(request)

    def delete_promotion(self, request):
        return promotion_controller.delete_promotion(request)
    

class DeliveryViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_delivery(self, request):
        return delivery_controller.create(request)

    def get_delivery(self, request):
        return delivery_controller.get_delivery(request)

    def update_delivery(self, request):
        return delivery_controller.update_delivery(request)

    def delete_delivery(self, request):
        return delivery_controller.delete_delivery(request)
    

class NotificationViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_notification(self, request):
        return notification_controller.create(request)

    def get_notification(self, request):
        return notification_controller.get_notification(request)

    def update_notification(self, request):
        return notification_controller.update_notification(request)

    def delete_notification(self, request):
        return notification_controller.delete_notification(request)
    

class CategoryViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_category(self, request):
        return category_controller.create(request)

    def get_category(self, request):
        return category_controller.get_category(request)

    def update_category(self, request):
        return category_controller.update_category(request)

    def delete_category(self, request):
        return category_controller.delete_category(request)
    

class ContactViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_contact(self, request):
        return contact_controller.create(request)

    def get_contact(self, request):
        return contact_controller.get_contact(request)

    def update_contact(self, request):
        return contact_controller.update_contact(request)

    def delete_contact(self, request):
        return contact_controller.delete_contact(request)
    

class OrderWithFSMViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_orderwithfms(self, request):
        return orderwithfsm_controller.create(request)

    def get_orderwithfms(self, request):
        return orderwithfsm_controller.get_orderwithfms(request)

    def update_orderwithfms(self, request):
        return orderwithfsm_controller.update_orderwithfms(request)

    def delete_orderwithfms(self, request):
        return orderwithfsm_controller.delete_orderwithfms(request)