from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext as _


class Route(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    """Name of route."""

    ticket_cost = models.DecimalField(verbose_name=_('Ticket cost'),
        decimal_places=2, max_digits=5)
    """Cost of ticket for single stop."""

    travel_time = models.CharField(verbose_name=_('Travel time'),
        max_length=40, null=True, blank=True)
    """Average travel time for route (used only for display)."""

    length = models.CharField(verbose_name=_('Route length'), max_length=255,
        null=True, blank=True)
    """Length of the route."""

    car_used = models.CharField(verbose_name=_('Car used'), max_length=100,
        null=True, blank=True)
    """What car is beign used to transport."""

    def __str__(self):
        return self.name


class Stop(models.Model):
    name = models.CharField(verbose_name=_('Stop name'), max_length=255)
    """Name of stop."""

    route = models.ForeignKey(Route, on_delete=models.CASCADE,
        verbose_name=_('Route'))
    """Describes to which route stop belongs."""

    time_table = ArrayField(models.TimeField())
    """Time table for stop."""

    def __str__(self):
        return self.name
