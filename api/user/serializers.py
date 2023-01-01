"""
Serializer for the user API
"""
from django.contrib.auth import get_user_model

from rest_framework import fields, serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'name']
