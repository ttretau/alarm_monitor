from rest_framework import authentication, permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Alarm
from .serializers import AlarmSerializer


class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )


class AlarmViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for alarm."""

    queryset = Alarm.objects.order_by("created")
    serializer_class = AlarmSerializer
    search_fields = ('title', 'text', 'closed')
    ordering_fields = ('created', 'closed')

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset
