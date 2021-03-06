from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import (AppointmentViewSet, ClientiewSet,
                    TrainerViewSet, AppointmentDayViewSet)

router = routers.DefaultRouter()
router.register('appointments', AppointmentViewSet)
router.register('trainers', TrainerViewSet)
router.register('clients', ClientiewSet)
router.register('days', AppointmentDayViewSet)
# router.register('days/detail/<int:pk>', AppointmentDayViewSet)
# router.register('days/{day}/detail/', AppointmentDayViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
