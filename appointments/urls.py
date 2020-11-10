from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import AppointmentViewSet, ClientiewSet, TrainerViewSet

router = routers.DefaultRouter()
router.register('appointments', AppointmentViewSet)
router.register('trainers', TrainerViewSet)
router.register('clients', ClientiewSet)


urlpatterns = [
    path('', include(router.urls)),
]
