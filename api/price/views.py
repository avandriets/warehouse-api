from rest_framework import (viewsets, permissions)
from core.models import PriceTypes
from price.serializers import PriceSerializer


class PriceTypesViewSet(viewsets.ModelViewSet):
    queryset = PriceTypes.objects.all()
    serializer_class = PriceSerializer
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
