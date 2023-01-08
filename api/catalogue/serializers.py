from rest_framework import serializers
from core.models import Catalogue


class CatalogueSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    updated_by = serializers.ReadOnlyField(source='updated_by.email')

    class Meta:
        model = Catalogue
        fields = ['id', 'name', 'description', 'owner', 'created_at', 'updated_at', 'updated_by']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at', 'updated_by']
