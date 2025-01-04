from apps.core.serializers import LogEntrySerializer
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django_filters import rest_framework as backend_filters
from rest_framework.permissions import IsAuthenticated
from utils.paginations import OurLimitOffsetPagination


class LogHistoryView(ListAPIView):
    serializer_class = LogEntrySerializer
    queryset = LogEntrySerializer.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = OurLimitOffsetPagination
