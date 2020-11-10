from rest_framework import serializers
from .models import Appointment
from api.serializers import UserSerializer
from .models import Client, Trainer, AppointmentDay


class TrainerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Trainer
        fields = ('id', 'user', 'full_name')


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Client
        fields = ('id', 'user', 'full_name')


class AppointmentDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = AppointmentDay
        fields = ('id', 'day')


class AppointmentSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True, many=False)
    client = ClientSerializer(read_only=True, many=False)
    day = AppointmentDaySerializer(read_only=True, many=False)

    class Meta:
        model = Appointment
        fields = ('id', 'day', 'start_time', 'time', 'trainer', 'client')
