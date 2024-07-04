from datetime import date, timedelta
from django.db import transaction
from django.utils import timezone
from django.contrib.auth import authenticate
from restaurent.filters import CategoryFilter, ContactFilter, DeliveryFilter, MenuFilter, MenuItemFilter, NotificationFilter, OrderFilter, PaymentFilter, PromotionFilter, RestaurantFilter, ReviewFilter
from restaurent.restaurent_serializer import *
from restaurent.models import Delivery, Restaurant
from utils.reusable_methods import get_first_error_message, generate_six_length_random_number
from rest_framework.response import Response
from django.db.models import Sum, Count, Avg, F
from utils.helper import create_response, paginate_data
from utils.response_messages import *
# from vehicle.serializer import serializer

# from chat_site.settings import EMAIL_HOST_USER
# from django.core.mail import send_mail
# from datetime import date, timedelta



class RestaurantController:
    serializer_class = RestaurantSerializer
    filterset_class = RestaurantFilter

 
    def create(self, request):
        try:
            request.POST._mutable = True
            request.data["created_by"] = request.user.guid
            request.POST._mutable = False

            # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
            validated_data = RestaurantSerializer(data=request.data)
            if validated_data.is_valid():
                response = validated_data.save()
                response_data = RestaurantSerializer(response).data
                return Response({'data': response_data}, 200)
            else:
                error_message = get_first_error_message(validated_data.errors, "UNSUCCESSFUL")
                return Response({'data': error_message}, 400)
            # else:
            #     return Response({'data': "Permission Denaied"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)

    # mydata = Member.objects.filter(firstname__endswith='s').values()
    def get_restaurant(self, request):
        try:

            instances = self.serializer_class.Meta.model.objects.all()

            filtered_data = self.filterset_class(request.GET, queryset=instances)
            data = filtered_data.qs

            paginated_data, count = paginate_data(data, request)

            serialized_data = self.serializer_class(paginated_data, many=True).data
            response_data = {
                "count": count,
                "data": serialized_data,
            }
            return create_response(response_data, "SUCCESSFUL", 200)


        except Exception as e:
            return Response({'error': str(e)}, 500)

    def update_restaurant(self, request):
        try:
            if "id" in request.data:
                # finding instance
                instance = Restaurant.objects.filter(id=request.data["id"]).first()

                if instance:
                    request.POST._mutable = True
                    request.data["updated_by"] = request.user.guid
                    request.POST._mutable = False

                    # updating the instance/record
                    serialized_data = RestaurantSerializer(instance, data=request.data, partial=True)
                    
                    if serialized_data.is_valid():
                        response = serialized_data.save()
                        response_data = RestaurantSerializer(response).data
                        return Response({"data": response_data}, 200)
                    else:
                        error_message = get_first_error_message(serialized_data.errors, "UNSUCCESSFUL")
                        return Response({'data': error_message}, 400)
                    
                else:
                    return Response({"data": "NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)

        except Exception as e:
            return Response({'error': str(e)}, 500)

    def delete_restaurant(self, request):
        try:
            if "id" in request.query_params:
                instance = Restaurant.objects.filter(id=request.query_params['id']).first()

                if instance:
                    instance.delete()
                    return Response({"data": "SUCESSFULL"}, 200)
                else:
                    return Response({"data": "RECORD NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)
        


class MenuController:
    serializer_class = MenuSerializer
    filterset_class = MenuFilter

 
    def create(self, request):
        try:
            request.POST._mutable = True
            request.data["created_by"] = request.user.guid
            request.POST._mutable = False

            validated_data = MenuSerializer(data=request.data)
            if validated_data.is_valid():
                response = validated_data.save()
                response_data = MenuSerializer(response).data
                return Response({'data': response_data}, 200)
            else:
                error_message = get_first_error_message(validated_data.errors, "UNSUCCESSFUL")
                return Response({'data': error_message}, 400)

        except Exception as e:
            return Response({'error': str(e)}, 500)

    def get_menu(self, request):
        try:

            instances = self.serializer_class.Meta.model.objects.all()

            filtered_data = self.filterset_class(request.GET, queryset=instances)
            data = filtered_data.qs

            paginated_data, count = paginate_data(data, request)

            serialized_data = self.serializer_class(paginated_data, many=True).data
            response_data = {
                "count": count,
                "data": serialized_data,
            }
            return create_response(response_data, "SUCCESSFUL", 200)


        except Exception as e:
            return Response({'error': str(e)}, 500)

    def update_menu(self, request):
        try:
            if "id" in request.data:
                # finding instance
                instance = Menu.objects.filter(id=request.data["id"]).first()

                if instance:
                    request.POST._mutable = True
                    request.data["updated_by"] = request.user.guid
                    request.POST._mutable = False

                    # updating the instance/record
                    serialized_data = MenuSerializer(instance, data=request.data, partial=True)
                    # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
                    if serialized_data.is_valid():
                        response = serialized_data.save()
                        response_data = MenuSerializer(response).data
                        return Response({"data": response_data}, 200)
                    else:
                        error_message = get_first_error_message(serialized_data.errors, "UNSUCCESSFUL")
                        return Response({'data': error_message}, 400)
                    # else:
                    #     return Response({'data': "Permission Denaied"}, 400)
                else:
                    return Response({"data": "NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)

        except Exception as e:
            return Response({'error': str(e)}, 500)

    def delete_menu(self, request):
        try:
            if "id" in request.query_params:
                instance = Menu.objects.filter(id=request.query_params['id']).first()

                if instance:
                    instance.delete()
                    return Response({"data": "SUCESSFULL"}, 200)
                else:
                    return Response({"data": "RECORD NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)
        

class MenuItemController:
    serializer_class = MenuItemSerializer
    filterset_class = MenuItemFilter

 
    def create(self, request):
        try:
            request.POST._mutable = True
            request.data["created_by"] = request.user.guid
            request.POST._mutable = False

            # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
            validated_data = MenuItemSerializer(data=request.data)
            if validated_data.is_valid():
                response = validated_data.save()
                response_data = MenuItemSerializer(response).data
                return Response({'data': response_data}, 200)
            else:
                error_message = get_first_error_message(validated_data.errors, "UNSUCCESSFUL")
                return Response({'data': error_message}, 400)
            # else:
            #     return Response({'data': "Permission Denaied"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)

    # mydata = Member.objects.filter(firstname__endswith='s').values()
    def get_menuitem(self, request):
        try:

            instances = self.serializer_class.Meta.model.objects.all()

            filtered_data = self.filterset_class(request.GET, queryset=instances)
            data = filtered_data.qs

            paginated_data, count = paginate_data(data, request)

            serialized_data = self.serializer_class(paginated_data, many=True).data
            response_data = {
                "count": count,
                "data": serialized_data,
            }
            return create_response(response_data, "SUCCESSFUL", 200)


        except Exception as e:
            return Response({'error': str(e)}, 500)

    def update_menuitem(self, request):
        try:
            if "id" in request.data:
                # finding instance
                instance = MenuItem.objects.filter(id=request.data["id"]).first()

                if instance:
                    request.POST._mutable = True
                    request.data["updated_by"] = request.user.guid
                    request.POST._mutable = False

                    # updating the instance/record
                    serialized_data = MenuItemSerializer(instance, data=request.data, partial=True)
                    # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
                    if serialized_data.is_valid():
                        response = serialized_data.save()
                        response_data = MenuItemSerializer(response).data
                        return Response({"data": response_data}, 200)
                    else:
                        error_message = get_first_error_message(serialized_data.errors, "UNSUCCESSFUL")
                        return Response({'data': error_message}, 400)
                    # else:
                    #     return Response({'data': "Permission Denaied"}, 400)
                else:
                    return Response({"data": "NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)

        except Exception as e:
            return Response({'error': str(e)}, 500)

    def delete_menuitem(self, request):
        try:
            if "id" in request.query_params:
                instance = MenuItem.objects.filter(id=request.query_params['id']).first()

                if instance:
                    instance.delete()
                    return Response({"data": "SUCESSFULL"}, 200)
                else:
                    return Response({"data": "RECORD NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)



class OrderController:
    serializer_class = OrderSerializer
    order_detail_serializer = OrderDetailSerializer
    filterset_class = OrderFilter

    def create(self, request):
        try:
            request.POST._mutable = True
            request.data["created_by"] = request.user.guid
            request.POST._mutable = False

            request.POST._mutable = True
            order_details = request.data.pop('OrderDetail') if 'OrderDetail' in request.data else None
            request.data['customer'] = request.user.guid
            today = date.today()
            if today.weekday() in [3,4]:
                delivery_days = timedelta(4)
            elif today.weekday() == 5:
                delivery_days = timedelta(3)
            else:
                delivery_days = timedelta(2)
            request.data['delivery_date'] = today + delivery_days
            request.data['status'] = 'booked'
            request.POST._mutable = False

            # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                with transaction.atomic():
                    response_data = serialized_data.save()
                    bill = 0
                    if order_details:
                        for i in order_details:
                            i['order'] = response_data.id
                            i['total_price'] = int(i['quantity']) * int(i['unit_price'])
                            bill += i['total_price']
                            serialized_detail = self.order_detail_serializer(data=i)
                            if serialized_detail.is_valid():
                                serialized_detail.save()
                            else:
                                transaction.set_rollback(True)
                                return create_response({}, get_first_error_message(serialized_detail.errors, UNSUCCESSFUL),400)
                        response_data.bill = bill
                        response_data.save()
        
                return create_response(self.serializer_class(response_data).data, SUCCESSFUL, 200)
            else:
                return create_response({}, get_first_error_message(serialized_data.errors,UNSUCCESSFUL), 400)
            # else:
            #     return Response({'data': "Permission Denaied"}, 400)
        except Exception as e:
            return create_response({'error':str(e)}, UNSUCCESSFUL, 500)
        
    def get_order(self, request):
        try:
            instances = self.serializer_class.Meta.model.objects.all()
            filtered_data = self.filterset_class(request.GET, queryset=instances)
            data = filtered_data.qs
            paginated_data, count = paginate_data(data, request)
            serialized_data = self.serializer_class(paginated_data, many=True).data
            response_data = {
                "count": count,
                "data": serialized_data,
            }
            return create_response(response_data, "SUCCESSFUL", 200)

        except Exception as e:
            return Response({'error': str(e)}, 500)

    def update_order(self, request):
        try:
            if 'id' in request.data:
                request.POST._mutable = True
                request.data["updated_by"] = request.user.guid
                request.POST._mutable = False
                
                instance = Order.objects.filter(id=request.data['id']).first()

                if instance:
                    request.POST._mutable = True
                    order_details = request.data.pop('OrderDetail') if "OrderDetail" in request.data else None
                    delete_order_details = request.data.pop('DeleteOrderDetail') if 'DeleteOrderDetail' in request.data else None
                    request.POST._mutable = False

                    serialized_data = self.serializer_class(instance, data=request.data, partial=True)
                    if serialized_data.is_valid():
                        response_data = serialized_data.save()
                        bill = 0

# if order_details === if order_details is not None
                        if order_details:
                            for i in order_details:
                                i['order'] = response_data.id
                                i['total_price'] = i['quantity'] * i['unit_price']
                                bill += i['total_price']
                                serialized_detail = self.order_detail_serializer(data=i)
                                if serialized_detail.is_valid():
                                    serialized_detail.save()
                                else:
                                    transaction.set_rollback(True)
                                    return create_response({}, get_first_error_message(serialized_detail.errors, UNSUCCESSFUL),400)
                            response_data.bill = bill
                            response_data.save()

                        if delete_order_details:
                            od = instance.order_detail_order.filter(id__in=delete_order_details)
                            # od = OrderDetails.objects.filter(id__in=delete_order_details)
                            if od:
                                od.delete()
                        return create_response(self.serializer_class(response_data).data, SUCCESSFUL, 200)
                    else:
                        return create_response({}, get_first_error_message(serialized_data.errors, UNSUCCESSFUL), 400)
                else:
                    return create_response({}, NOT_FOUND, 404)
            else:
                return create_response({}, ID_NOT_PROVIDED, 400)
        except Exception as e:
            return create_response({'error':str(e)}, UNSUCCESSFUL, 500)

    def delete_order(self, request):
        try:
            if "id" in request.query_params:
                instance = Order.objects.filter(id=request.query_params['id']).first()
                if instance:
                    instance.delete()
                    return Response({"data": "SUCESSFULL"}, 200)
                else:
                    return Response({"data": "RECORD NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)

        except Exception as e:
            return Response({'error': str(e)}, 500)



class PaymentController:
    serializer_class = PaymentSerializer
    filterset_class = PaymentFilter

 
    def create(self, request):
        try:
            request.POST._mutable = True
            request.data["created_by"] = request.user.guid
            request.POST._mutable = False

            # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
            validated_data = PaymentSerializer(data=request.data)
            if validated_data.is_valid():
                response = validated_data.save()
                response_data = PaymentSerializer(response).data
                return Response({'data': response_data}, 200)
            else:
                error_message = get_first_error_message(validated_data.errors, "UNSUCCESSFUL")
                return Response({'data': error_message}, 400)
            # else:
            #     return Response({'data': "Permission Denaied"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)

    # mydata = Member.objects.filter(firstname__endswith='s').values()
    def get_payment(self, request):
        try:

            instances = self.serializer_class.Meta.model.objects.all()

            filtered_data = self.filterset_class(request.GET, queryset=instances)
            data = filtered_data.qs

            paginated_data, count = paginate_data(data, request)

            serialized_data = self.serializer_class(paginated_data, many=True).data
            response_data = {
                "count": count,
                "data": serialized_data,
            }
            return create_response(response_data, "SUCCESSFUL", 200)


        except Exception as e:
            return Response({'error': str(e)}, 500)

    def update_payment(self, request):
        try:
            if "id" in request.data:
                # finding instance
                instance = Payment.objects.filter(id=request.data["id"]).first()

                if instance:
                    request.POST._mutable = True
                    request.data["updated_by"] = request.user.guid
                    request.POST._mutable = False

                    # updating the instance/record
                    serialized_data = PaymentSerializer(instance, data=request.data, partial=True)
                    # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
                    if serialized_data.is_valid():
                        response = serialized_data.save()
                        response_data = PaymentSerializer(response).data
                        return Response({"data": response_data}, 200)
                    else:
                        error_message = get_first_error_message(serialized_data.errors, "UNSUCCESSFUL")
                        return Response({'data': error_message}, 400)
                    # else:
                    #     return Response({'data': "Permission Denaied"}, 400)
                else:
                    return Response({"data": "NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)

        except Exception as e:
            return Response({'error': str(e)}, 500)

    def delete_payment(self, request):
        try:
            if "id" in request.query_params:
                instance = Payment.objects.filter(id=request.query_params['id']).first()

                if instance:
                    instance.delete()
                    return Response({"data": "SUCESSFULL"}, 200)
                else:
                    return Response({"data": "RECORD NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)



class ReviewController:
    serializer_class = ReviewSerializer
    filterset_class = ReviewFilter

 
    def create(self, request):
        try:
            request.POST._mutable = True
            request.data["created_by"] = request.user.guid
            request.POST._mutable = False

            # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
            validated_data = ReviewSerializer(data=request.data)
            if validated_data.is_valid():
                response = validated_data.save()
                response_data = ReviewSerializer(response).data
                return Response({'data': response_data}, 200)
            else:
                error_message = get_first_error_message(validated_data.errors, "UNSUCCESSFUL")
                return Response({'data': error_message}, 400)
            # else:
            #     return Response({'data': "Permission Denaied"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)

    # mydata = Member.objects.filter(firstname__endswith='s').values()
    def get_review(self, request):
        try:

            instances = self.serializer_class.Meta.model.objects.all()

            filtered_data = self.filterset_class(request.GET, queryset=instances)
            data = filtered_data.qs

            paginated_data, count = paginate_data(data, request)

            serialized_data = self.serializer_class(paginated_data, many=True).data
            response_data = {
                "count": count,
                "data": serialized_data,
            }
            return create_response(response_data, "SUCCESSFUL", 200)


        except Exception as e:
            return Response({'error': str(e)}, 500)

    def update_review(self, request):
        try:
            if "id" in request.data:
                # finding instance
                instance = Review.objects.filter(id=request.data["id"]).first()

                if instance:
                    request.POST._mutable = True
                    request.data["updated_by"] = request.user.guid
                    request.POST._mutable = False

                    # updating the instance/record
                    serialized_data = ReviewSerializer(instance, data=request.data, partial=True)
                    # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
                    if serialized_data.is_valid():
                        response = serialized_data.save()
                        response_data = ReviewSerializer(response).data
                        return Response({"data": response_data}, 200)
                    else:
                        error_message = get_first_error_message(serialized_data.errors, "UNSUCCESSFUL")
                        return Response({'data': error_message}, 400)
                    # else:
                    #     return Response({'data': "Permission Denaied"}, 400)
                else:
                    return Response({"data": "NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)

        except Exception as e:
            return Response({'error': str(e)}, 500)

    def delete_review(self, request):
        try:
            if "id" in request.query_params:
                instance = Review.objects.filter(id=request.query_params['id']).first()

                if instance:
                    instance.delete()
                    return Response({"data": "SUCESSFULL"}, 200)
                else:
                    return Response({"data": "RECORD NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)
        

class PromotionController:
    serializer_class = PromotionSerializer
    filterset_class = PromotionFilter

 
    def create(self, request):
        try:
            request.POST._mutable = True
            request.data["created_by"] = request.user.guid
            request.POST._mutable = False

            # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
            validated_data = PromotionSerializer(data=request.data)
            if validated_data.is_valid():
                response = validated_data.save()
                response_data = PromotionSerializer(response).data
                return Response({'data': response_data}, 200)
            else:
                error_message = get_first_error_message(validated_data.errors, "UNSUCCESSFUL")
                return Response({'data': error_message}, 400)
            # else:
            #     return Response({'data': "Permission Denaied"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)

    # mydata = Member.objects.filter(firstname__endswith='s').values()
    def get_promotion(self, request):
        try:

            instances = self.serializer_class.Meta.model.objects.all()

            filtered_data = self.filterset_class(request.GET, queryset=instances)
            data = filtered_data.qs

            paginated_data, count = paginate_data(data, request)

            serialized_data = self.serializer_class(paginated_data, many=True).data
            response_data = {
                "count": count,
                "data": serialized_data,
            }
            return create_response(response_data, "SUCCESSFUL", 200)


        except Exception as e:
            return Response({'error': str(e)}, 500)

    def update_promotion(self, request):
        try:
            if "id" in request.data:
                # finding instance
                instance = Promotion.objects.filter(id=request.data["id"]).first()

                if instance:
                    request.POST._mutable = True
                    request.data["updated_by"] = request.user.guid
                    request.POST._mutable = False

                    # updating the instance/record
                    serialized_data = PromotionSerializer(instance, data=request.data, partial=True)
                    # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
                    if serialized_data.is_valid():
                        response = serialized_data.save()
                        response_data = PromotionSerializer(response).data
                        return Response({"data": response_data}, 200)
                    else:
                        error_message = get_first_error_message(serialized_data.errors, "UNSUCCESSFUL")
                        return Response({'data': error_message}, 400)
                    # else:
                    #     return Response({'data': "Permission Denaied"}, 400)
                else:
                    return Response({"data": "NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)

        except Exception as e:
            return Response({'error': str(e)}, 500)

    def delete_promotion(self, request):
        try:
            if "id" in request.query_params:
                instance = Promotion.objects.filter(id=request.query_params['id']).first()

                if instance:
                    instance.delete()
                    return Response({"data": "SUCESSFULL"}, 200)
                else:
                    return Response({"data": "RECORD NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)
        



class DeliveryController:
    serializer_class = DeliverySerializer
    filterset_class = DeliveryFilter

 
    def create(self, request):
        try:
            request.POST._mutable = True
            request.data["created_by"] = request.user.guid
            request.POST._mutable = False

            # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
            validated_data = DeliverySerializer(data=request.data)
            if validated_data.is_valid():
                response = validated_data.save()
                response_data = DeliverySerializer(response).data
                return Response({'data': response_data}, 200)
            else:
                error_message = get_first_error_message(validated_data.errors, "UNSUCCESSFUL")
                return Response({'data': error_message}, 400)
            # else:
            #     return Response({'data': "Permission Denaied"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)

    # mydata = Member.objects.filter(firstname__endswith='s').values()
    def get_delivery(self, request):
        try:

            instances = self.serializer_class.Meta.model.objects.all()

            filtered_data = self.filterset_class(request.GET, queryset=instances)
            data = filtered_data.qs

            paginated_data, count = paginate_data(data, request)

            serialized_data = self.serializer_class(paginated_data, many=True).data
            response_data = {
                "count": count,
                "data": serialized_data,
            }
            return create_response(response_data, "SUCCESSFUL", 200)


        except Exception as e:
            return Response({'error': str(e)}, 500)

    def update_delivery(self, request):
        try:
            if "id" in request.data:
                # finding instance
                instance = Delivery.objects.filter(id=request.data["id"]).first()

                if instance:
                    request.POST._mutable = True
                    request.data["updated_by"] = request.user.guid
                    request.POST._mutable = False

                    # updating the instance/record
                    serialized_data = DeliverySerializer(instance, data=request.data, partial=True)
                    # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
                    if serialized_data.is_valid():
                        response = serialized_data.save()
                        response_data = DeliverySerializer(response).data
                        return Response({"data": response_data}, 200)
                    else:
                        error_message = get_first_error_message(serialized_data.errors, "UNSUCCESSFUL")
                        return Response({'data': error_message}, 400)
                    # else:
                    #     return Response({'data': "Permission Denaied"}, 400)
                else:
                    return Response({"data": "NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)

        except Exception as e:
            return Response({'error': str(e)}, 500)

    def delete_delivery(self, request):
        try:
            if "id" in request.query_params:
                instance = Delivery.objects.filter(id=request.query_params['id']).first()

                if instance:
                    instance.delete()
                    return Response({"data": "SUCESSFULL"}, 200)
                else:
                    return Response({"data": "RECORD NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)
        

class NotificationController:
    serializer_class = NotificationSerializer
    filterset_class = NotificationFilter

 
    def create(self, request):
        try:
            request.POST._mutable = True
            request.data["created_by"] = request.user.guid
            request.POST._mutable = False

            # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
            validated_data = NotificationSerializer(data=request.data)
            if validated_data.is_valid():
                response = validated_data.save()
                response_data = NotificationSerializer(response).data
                return Response({'data': response_data}, 200)
            else:
                error_message = get_first_error_message(validated_data.errors, "UNSUCCESSFUL")
                return Response({'data': error_message}, 400)
            # else:
            #     return Response({'data': "Permission Denaied"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)

    # mydata = Member.objects.filter(firstname__endswith='s').values()
    def get_notification(self, request):
        try:

            instances = self.serializer_class.Meta.model.objects.all()

            filtered_data = self.filterset_class(request.GET, queryset=instances)
            data = filtered_data.qs

            paginated_data, count = paginate_data(data, request)

            serialized_data = self.serializer_class(paginated_data, many=True).data
            response_data = {
                "count": count,
                "data": serialized_data,
            }
            return create_response(response_data, "SUCCESSFUL", 200)


        except Exception as e:
            return Response({'error': str(e)}, 500)

    def update_notification(self, request):
        try:
            if "id" in request.data:
                # finding instance
                instance = Notification.objects.filter(id=request.data["id"]).first()

                if instance:
                    request.POST._mutable = True
                    request.data["updated_by"] = request.user.guid
                    request.POST._mutable = False

                    # updating the instance/record
                    serialized_data = NotificationSerializer(instance, data=request.data, partial=True)
                    # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
                    if serialized_data.is_valid():
                        response = serialized_data.save()
                        response_data = NotificationSerializer(response).data
                        return Response({"data": response_data}, 200)
                    else:
                        error_message = get_first_error_message(serialized_data.errors, "UNSUCCESSFUL")
                        return Response({'data': error_message}, 400)
                    # else:
                    #     return Response({'data': "Permission Denaied"}, 400)
                else:
                    return Response({"data": "NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)

        except Exception as e:
            return Response({'error': str(e)}, 500)

    def delete_notification(self, request):
        try:
            if "id" in request.query_params:
                instance = Notification.objects.filter(id=request.query_params['id']).first()

                if instance:
                    instance.delete()
                    return Response({"data": "SUCESSFULL"}, 200)
                else:
                    return Response({"data": "RECORD NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)
        


class CategoryController:
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter

 
    def create(self, request):
        try:
            request.POST._mutable = True
            request.data["created_by"] = request.user.guid
            request.POST._mutable = False

            # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
            validated_data = CategorySerializer(data=request.data)
            if validated_data.is_valid():
                response = validated_data.save()
                response_data = CategorySerializer(response).data
                return Response({'data': response_data}, 200)
            else:
                error_message = get_first_error_message(validated_data.errors, "UNSUCCESSFUL")
                return Response({'data': error_message}, 400)
            # else:
            #     return Response({'data': "Permission Denaied"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)

    # mydata = Member.objects.filter(firstname__endswith='s').values()
    def get_category(self, request):
        try:

            instances = self.serializer_class.Meta.model.objects.all()

            filtered_data = self.filterset_class(request.GET, queryset=instances)
            data = filtered_data.qs

            paginated_data, count = paginate_data(data, request)

            serialized_data = self.serializer_class(paginated_data, many=True).data
            response_data = {
                "count": count,
                "data": serialized_data,
            }
            return create_response(response_data, "SUCCESSFUL", 200)


        except Exception as e:
            return Response({'error': str(e)}, 500)

    def update_category(self, request):
        try:
            if "id" in request.data:
                # finding instance
                instance = Category.objects.filter(id=request.data["id"]).first()

                if instance:
                    request.POST._mutable = True
                    request.data["updated_by"] = request.user.guid
                    request.POST._mutable = False

                    # updating the instance/record
                    serialized_data = CategorySerializer(instance, data=request.data, partial=True)
                    # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
                    if serialized_data.is_valid():
                        response = serialized_data.save()
                        response_data = CategorySerializer(response).data
                        return Response({"data": response_data}, 200)
                    else:
                        error_message = get_first_error_message(serialized_data.errors, "UNSUCCESSFUL")
                        return Response({'data': error_message}, 400)
                    # else:
                    #     return Response({'data': "Permission Denaied"}, 400)
                else:
                    return Response({"data": "NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)

        except Exception as e:
            return Response({'error': str(e)}, 500)

    def delete_category(self, request):
        try:
            if "id" in request.query_params:
                instance = Category.objects.filter(id=request.query_params['id']).first()

                if instance:
                    instance.delete()
                    return Response({"data": "SUCESSFULL"}, 200)
                else:
                    return Response({"data": "RECORD NOT FOUND"}, 404)
            else:
                return Response({"data": "ID NOT PROVIDED"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)


class ContactController:
    serializer_class = ContactSerializer
    filterset_class = ContactFilter

 
    def create(self, request):
        try:
            request.POST._mutable = True
            request.data["created_by"] = request.user.guid
            request.POST._mutable = False

            # if request.user.role in ['admin', 'manager'] or request.user.is_superuser:  # roles
            validated_data = ContactSerializer(data=request.data)
            if validated_data.is_valid():
                response = validated_data.save()
                response_data = ContactSerializer(response).data
                return Response({'data': response_data}, 200)
            else:
                error_message = get_first_error_message(validated_data.errors, "UNSUCCESSFUL")
                return Response({'data': error_message}, 400)
            # else:
            #     return Response({'data': "Permission Denaied"}, 400)
        except Exception as e:
            return Response({'error': str(e)}, 500)

    # mydata = Member.objects.filter(firstname__endswith='s').values()
    def get_contact(self, request):
        try:

            instances = self.serializer_class.Meta.model.objects.all()

            filtered_data = self.filterset_class(request.GET, queryset=instances)
            data = filtered_data.qs

            paginated_data, count = paginate_data(data, request)

            serialized_data = self.serializer_class(paginated_data, many=True).data
            response_data = {
                "count": count,
                "data": serialized_data,
            }
            return create_response(response_data, "SUCCESSFUL", 200)


        except Exception as e:
            return Response({'error': str(e)}, 500)

   

