from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from paypalcheckoutsdk.orders import OrdersGetRequest
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from apps.booking.models import Bookings
from apps.payments_and_subscription.serializers import PaypalUserDetailsSerializer, PaymentDetailsSerializers
from apps.payments_and_subscription.models import Subscription


class CreatePaypalUserDetailsView(CreateAPIView):
    serializer_class = PaypalUserDetailsSerializer
    permission_classes = [IsAuthenticated]
    queryset = PaypalUserDetailsSerializer.Meta.model.objects.all()

    def create(self, request, *args, **kwargs):
        if PaypalUserDetailsSerializer.Meta.model.objects.filter(user=request.user.profile).exists():
            return Response({
                'message': 'Paypal user details already exists'
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializers = self.get_serializer(data=request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save(user=request.user.profile)
            return Response({
                'message': 'Paypal user details created successfully',
                'data': serializers.data
            }, status=status.HTTP_201_CREATED)


class PaypalUserDetailsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaypalUserDetailsSerializer
    permission_classes = [IsAuthenticated]
    queryset = PaypalUserDetailsSerializer.Meta.model.objects.all()

    def get_object(self):
        return self.request.user.profile.paypal_user_details


class CreatePayPalPaymentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            paypal_payment_id = request.data.get('paypal_payment_id', None)
            subscription_id = request.data.get('subscription_id', None)
            amount = request.data.get('amount', None)
            payment_for = request.data.get('payment_for', None)
            booking = request.data.get('booking', None)

            if payment_for == 'subscription':

                if not paypal_payment_id or not subscription_id or not amount:
                    return Response({
                        'message': 'paypal_payment_id, subscription_id and amount are required'
                    }, status=status.HTTP_400_BAD_REQUEST)
                if paypal_payment_id and subscription_id and amount:
                    subscription = get_object_or_404(Subscription, id=subscription_id)
                    if subscription.subscription_price != amount:
                        return Response({
                            'message': 'Amount does not match with subscription price'
                        }, status=status.HTTP_400_BAD_REQUEST)
                    paypal_client = settings.PAYPAL_CLIENT
                    response = paypal_client.execute(
                        OrdersGetRequest(paypal_payment_id))
                    paid_amount = response.result.purchase_units[0].amount.value
                    paid_currency = response.result.purchase_units[0].amount.currency_code
                    transaction_time = response.result.create_time
                    payment_resource_id = response.result.purchase_units[0].payments.captures[0].id
                    if paid_amount != amount:
                        return Response({
                            'message': 'Amount does not match with subscription price'
                        }, status=status.HTTP_400_BAD_REQUEST)
                    payment = PaymentDetailsSerializers.Meta.model.objects.create(
                        user=request.user.profile,
                        payment_id=paypal_payment_id,
                        subscription_id=subscription_id,
                        paid_amount=paid_amount,
                        paid_currency=paid_currency,
                        payment_time=transaction_time,
                        payment_resource_id=payment_resource_id
                    )
                    if response.result.status == 'SUCCESS':
                        user = request.user.profile
                        user.subscription = subscription
                        user.profile_status='active'
                        user.is_subscribed = True
                        user.subscription_start_date = transaction_time
                        user.subscription_end_date = payment.payment_time + timedelta(
                            days=subscription.subscription_duration_days)
                        user.save()

                    return Response({
                        'message': 'Payment created successfully',
                        'data': PaymentDetailsSerializers(payment).data
                    }, status=status.HTTP_201_CREATED)
            elif payment_for == 'booking':
                if not paypal_payment_id or not booking or not amount:
                    return Response({
                        'message': 'paypal_payment_id, booking and amount are required'
                    }, status=status.HTTP_400_BAD_REQUEST)
                if paypal_payment_id and booking and amount:
                    booking = get_object_or_404(Bookings, id=booking)
                    if booking.total_price != amount:
                        return Response({
                            'message': 'Amount does not match with booking price'
                        }, status=status.HTTP_400_BAD_REQUEST)
                    paypal_client = settings.PAYPAL_CLIENT
                    response = paypal_client.execute(
                        OrdersGetRequest(paypal_payment_id))
                    paid_amount = response.result.purchase_units[0].amount.value
                    paid_currency = response.result.purchase_units[0].amount.currency_code
                    transaction_time = response.result.create_time
                    payment_resource_id = response.result.purchase_units[0].payments.captures[0].id
                    if paid_amount != amount:
                        return Response({
                            'message': 'Amount does not match with booking price'
                        }, status=status.HTTP_400_BAD_REQUEST)
                    payment = PaymentDetailsSerializers.Meta.model.objects.create(
                        user=request.user.profile,
                        payment_id=paypal_payment_id,
                        booking_id=booking.id,
                        paid_amount=paid_amount,
                        paid_currency=paid_currency,
                        payment_time=transaction_time,
                        payment_resource_id=payment_resource_id
                    )
                    if response.result.status == 'SUCCESS':
                        booking.payment_status = 'Confirmed'
                        booking.save()
                        return Response({
                            'message': 'Payment created successfully',
                        }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'message': 'Invalid payment type'
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
