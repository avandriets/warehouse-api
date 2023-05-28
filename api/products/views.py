from rest_framework import (viewsets, permissions)
from core.models import Products
from products.serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
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
