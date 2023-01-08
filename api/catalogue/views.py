from rest_framework import (viewsets, permissions)
from catalogue.serializers import CatalogueSerializer
from core.models import Catalogue


class CatalogueViewSet(viewsets.ModelViewSet):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer
    permission_classes = [permissions.IsAuthenticated]
    keycloak_scopes = {
        'GET': 'view',
        'POST': 'edit',
        'PATCH': 'edit',
        'PUT': 'edit',
        'DELETE': 'edit'
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
