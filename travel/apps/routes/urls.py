from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'routes', views.RouteViewset)

urlpatterns = [
    path('stops/<int:pk>/', views.GetStops().as_view(), name="get_stops")
] + router.urls