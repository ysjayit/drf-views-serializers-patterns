from rest_framework import serializers
from .models import Type, Vehicle


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['url', 'id', 'name']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.HyperlinkedRelatedField(
        queryset = Type.objects.all(),
        view_name = 'type-detail'
    )


    class Meta:
        model = Vehicle
        fields = ['url', 'id', 'name', 'description', 'price', 'type']
