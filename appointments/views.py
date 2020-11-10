from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import AppointmentSerializer, TrainerSerializer, ClientSerializer
from .models import Appointment, Trainer, Client
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from datetime import timedelta, datetime


# Create your views here.


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class ClientiewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    @action(detail=False, methods=['POST'])
    def book_app(self, request):

        day = request.data['day']
        start_time = request.data['start_time']
        end_time = request.data['end_time']
        trainer = request.data['trainer_id']
        client = request.data['client_id']
        time = None

        trainer_instance = Trainer.objects.get(id=trainer)
        client_instance = Client.objects.get(id=client)

        if not start_time or not end_time:
            pass
        else:
            time1 = datetime.strptime(str(end_time), '%H:%M:%S')
            time2 = datetime.strptime(str(start_time), '%H:%M:%S')
            difference = time1-time2
            total = 0
            acc = str(difference).split(":")
            total = total + int(acc[0]) * 60
            total = total + int(acc[1])
            time = total

        appointment = Appointment.objects.create(
            trainer=trainer_instance, client=client_instance, day=day, start_time=start_time, end_time=end_time, time=time)
        serializer = AppointmentSerializer(appointment, many=False)

        message = {'msg': "Appt Booked!", 'appointment': serializer.data}
        return Response(message, status=status.HTTP_200_OK)
