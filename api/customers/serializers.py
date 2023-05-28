from rest_framework import serializers
from core.models import Customers


class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    updated_by = serializers.ReadOnlyField(source='updated_by.email')

    class Meta:
        model = Customers
        fields = [
            'id',
            'name',
            'address',
            'tax_number',
            'seller',
            'description',
            'owner',
            'created_at',
            'updated_at',
            'updated_by',
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at', 'updated_by']
