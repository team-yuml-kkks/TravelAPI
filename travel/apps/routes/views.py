from django.shortcuts import get_object_or_404

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet

from .models import Route, Stop
from .serializers import RouteSerializer, StopSerializer


class RouteViewset(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    model = Route
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class GetStops(ListAPIView):
    model = Stop
    serializer_class = StopSerializer

    def get_queryset(self):
        route = get_object_or_404(Route, pk=self.kwargs.get('pk', None))
        return Stop.objects.filter(route=route)
