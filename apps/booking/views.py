from rest_framework import viewsets
from .serializers import BookingsSerializer, ClientFeedbackSerializer, ServiceFeedbackSerializer, JournalsSerializer, BookingUserSerializer
from rest_framework import filters
from apps.services.models import  CompanyStaff
from rest_framework.views import APIView
from django_filters import rest_framework as backend_filters
from .filters import BookingsFilter
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from utils.paginations import OurLimitOffsetPagination
from apps.userprofile.models import UserProfile
from datetime import datetime
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from django.db.models import Count
import calendar

class BookingDashboard(APIView):
    def get(self, request):
        try:
            # Get bookings for the current user's company
            booking_list = BookingsSerializer.Meta.model.objects.filter(
                service__company__owner=request.user.profile
            )

            # Aggregate bookings by month using booking_date
            monthly_bookings = booking_list.annotate(
                month=ExtractMonth('booking_date')  # Using booking_date for aggregation
            ).values('month').annotate(
                count=Count('id')
            ).order_by('month')

            # Initialize a dictionary to hold the counts for each month
            bookings_per_month = {i: 0 for i in range(1, 13)}

            # Populate the dictionary with the aggregated data
            for booking in monthly_bookings:
                bookings_per_month[booking['month']] = booking['count']

            # Create a list of month names with their corresponding counts
            month_names = {i: calendar.month_name[i] for i in range(1, 13)}
            result = {month_names[i]: bookings_per_month[i] for i in range(1, 13)}

            return Response(result)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

class DashboardUserOccupancy(APIView):
    def get(self, request):
        try:
            # Get bookings for the current user's company
            company_staff = CompanyStaff.objects.filter(company__owner=request.user.profile)


            # Aggregate bookings by month using booking_date
            monthly_occupancy = company_staff.annotate(
                month=ExtractMonth('work_from')  # Using booking_date for aggregation
            ).values('month').annotate(
                count=Count('id')
            ).order_by('month')

            # Initialize a dictionary to hold the counts for each month
            occupancy_per_month = {i: 0 for i in range(1, 13)}

            # Populate the dictionary with the aggregated data
            for booking in monthly_occupancy:
                occupancy_per_month[booking['month']] = booking['count']

            # Create a list of month names with their corresponding counts
            month_names = {i: calendar.month_name[i] for i in range(1, 13)}
            result = {month_names[i]: occupancy_per_month[i] for i in range(1, 13)}

            return Response(result)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

class BookingPIChart(APIView):
    def get(self, request):
        try:
            # Get bookings for the current user's company
            booking_list = BookingsSerializer.Meta.model.objects.filter(
                service__company__owner=request.user.profile
            ).values('booking_status').annotate(
                count=Count('id')
            )

            booking_status_dict = {status['booking_status']: _status['count'] for _status in booking_list}
            return Response(booking_status_dict)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class BookingUsersList(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = BookingUserSerializer
    pagination_class = OurLimitOffsetPagination
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    search_fields = ['first_name', 'last_name', 'user__email', ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_fields = ['user','user__email']

    def get_queryset(self):
        queryset = self.queryset.filter(user__user_type='client')
        return queryset


class BookingDetailsForCalenderListing(APIView):
    def get(self, request):
        try:
            month = request.GET.get('month',None)
            year = request.GET.get('year',None)
            booking_list = BookingsSerializer.Meta.model.objects.filter(
                service__company__owner=request.user.profile)
            if not month and not year:
                month = datetime.now().month
                year = datetime.now().year
            if month and year:
                booking_list = BookingsSerializer.Meta.model.objects.filter(service__company__owner=request.user.profile, booking_date__month=month, booking_date__year=year)
            booking_list = booking_list.values('id', 'booking_date', 'start_booking_slot', 'end_booking_slot', 'service', 'service__service_name', 'booking_status')
            return Response(booking_list, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class JournalsViewSet(viewsets.ModelViewSet):
    serializer_class = JournalsSerializer
    queryset = JournalsSerializer.Meta.model.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    search_fields = ['name', 'description']
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_fields = ['name', 'description']
    pagination_class = OurLimitOffsetPagination
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user.profile)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)



class ClientFeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = ClientFeedbackSerializer
    queryset = ClientFeedbackSerializer.Meta.model.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_fields = ['rating', 'feedback']
    pagination_class = OurLimitOffsetPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'owner':
                return self.queryset.filter(booking__service__company__owner=self.request.user.profile)
            return self.queryset.filter(user=self.request.user.profile)
        return self.queryset.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user.profile)

class ServiceFeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceFeedbackSerializer
    queryset = ServiceFeedbackSerializer.Meta.model.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_fields = ['rating', 'feedback']
    pagination_class = OurLimitOffsetPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'owner':
                return self.queryset.filter(service__company__owner=self.request.user.profile)
            return self.queryset.filter(user=self.request.user.profile)
        return self.queryset.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user.profile)


class BookingsViewSet(viewsets.ModelViewSet):
    serializer_class = BookingsSerializer
    queryset = BookingsSerializer.Meta.model.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    search_fields = ['name', 'description', 'total_price']
    ordering_fields = ['id', 'total_price', 'created_at', 'updated_at']
    filterset_class = BookingsFilter
    pagination_class = OurLimitOffsetPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'owner':
                return self.queryset.filter(service__company__owner=self.request.user.profile)
            return self.queryset.filter(user=self.request.user.profile)
        return self.queryset.none()

    def perform_create(self, serializer):
        serializer.save()
        instance = serializer.instance
        additional_services = instance.service.additional_services.all()
        total_price= instance.service.price
        if additional_services.exists():
            for service in additional_services:
                if service.is_free:
                    total_price += service.price
        instance.total_price = total_price
        instance.save()
    def perform_update(self, serializer):
        instance = serializer.instance
        additional_services = instance.service.additional_services.all()
        total_price= instance.service.price
        if additional_services.exists():
            for service in additional_services:
                if service.is_free:
                    total_price += service.price
        serializer.save(total_price=total_price)



