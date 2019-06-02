from rest_framework.serializers import ModelSerializer

from .models import Route, Stop


class RouteSerializer(ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'name', 'ticket_cost', 'travel_time',
            'length', 'car_used')


class StopSerializer(ModelSerializer):
    class Meta:
        model = Stop
        fields = ('id', 'name', 'route', 'time_table')
