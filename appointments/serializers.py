from rest_framework import serializers
from .models import Appointment
from api.serializers import UserSerializer
from .models import Client, Trainer


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


class AppointmentSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True, many=False)
    client = ClientSerializer(read_only=True, many=False)

    class Meta:
        model = Appointment
        fields = ('trainer', 'client', 'day', 'start_time', 'time')
