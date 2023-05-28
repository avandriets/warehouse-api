from rest_framework import serializers

from catalogue.serializers import CatalogueSerializer
from core.models import Products, Catalogue


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    updated_by = serializers.ReadOnlyField(source='updated_by.email')
    # category_details = serializers.PrimaryKeyRelatedField(
    #     required=False,
    #     queryset=Catalogue.objects.all(),
    #     many=False)
    # category_details = CatalogueSerializer(read_only=True, source='category')
    # category_details = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='catalogue'
    # )
    # category = serializers.ReadOnlyField()
    # category = serializers.HyperlinkedRelatedField(
    #     view_name='category-detail',
    #     read_only=True,
    #     # lookup_field='category'
    # )

    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'printName',
            'barcode',
            'category',
            # 'category_details',
            'product_code',
            'height',
            'width',
            'length',
            'weight',
            'description',
            'owner',
            'created_at',
            'updated_at',
            'updated_by',
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at', 'updated_by']
