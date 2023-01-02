from rest_framework import generics, authentication, permissions
from rest_framework.response import Response

from user.serializers import (UserSerializer)


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    # keycloak_scopes = {
    #     'GET': 'view',
    #     'POST': 'edit',
    #     'PUT': 'edit',
    #     'DELETE': 'edit'
    # }

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
