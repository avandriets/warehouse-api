from rest_framework import (viewsets, permissions, filters)
from catalogue.serializers import CatalogueSerializer
from core.models import Catalogue
from django_filters import rest_framework as filters
import django_filters


class CatalogueFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')


class CatalogueViewSet(viewsets.ModelViewSet):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = {
        'name': [
            'icontains',
            'exact',
        ],
        'description': [
            'icontains',
        ]}

    search_fields = ['$name', '$description']
    ordering_fields = '__all__'

    keycloak_scopes = {
        'GET': 'view',
        'POST': 'edit',
        'PATCH': 'edit',
        'PUT': 'edit',
        'DELETE': 'edit'
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
