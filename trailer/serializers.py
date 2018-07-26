from rest_framework import serializers
from .models import Vehicles, Trailer
import logging

logger = logging.getLogger('serializers.py')


class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('id', 'load_id', 'reference_id', 'vehicle', 'pickup',  'delivery', 'mileage', 'price', 'company',
                  'phone', 'hour', 'note', 'posted', 'ship', 'scraped_date', 'updated_date')

    def create(self, validated_data):
        return Vehicles.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.load_id = validated_data.get('load_id', instance.title)
        return instance


class TrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = ('id', 'trailer', 'capacity', 'miles_per_gallon', 'cost_per_gallon', 'pick_up_state',
                  'pick_up_city', 'pick_up_radius', 'delivery', 'delivery_radius', 'minimum_cost_per_mile',
                  'create_date', 'update_date')

    def create(self, validated_data):
        return Trailer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.trailer = validated_data.get('trailer', instance.trailer)
        instance.number_of_cars = validated_data.get('capacity', instance.capacity)
        instance.miles_per_gallon = validated_data.get('miles_per_gallon', instance.miles_per_gallon)
        instance.cost_per_gallon = validated_data.get('cost_per_gallon', instance.cost_per_gallon)
        instance.pick_up_state = validated_data.get('pick_up_state', instance.pick_up_state)
        instance.pick_up_city = validated_data.get('pick_up_city', instance.pick_up_city)
        instance.pick_up_radius = validated_data.get('pick_up_radius', instance.pick_up_radius)
        instance.delivery = validated_data.get('delivery', instance.delivery)
        instance.delivery_radius = validated_data.get('delivery_radius', instance.delivery_radius)
        instance.minimum_cost_per_mile = validated_data.get('minimum_cost_per_mile', instance.minimum_cost_per_mile)
        instance.create_date = validated_data.get('create_date', instance.create_date)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.save()
        return instance
