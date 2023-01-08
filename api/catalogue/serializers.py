from rest_framework import serializers

from core.models import Catalogue


class CatalogueSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Catalogue
        fields = ['id', 'name', 'description', 'owner']
        read_only_fields = ['id', 'owner']
