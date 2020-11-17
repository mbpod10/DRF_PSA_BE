from django.shortcuts import render
from rest_framework import viewsets, status
# , DayListSerializer
from .serializers import (AppointmentSerializer, TrainerSerializer,
                          ClientSerializer, AppointmentDaySerializer)
from .models import Appointment, Trainer, Client, AppointmentDay
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

    @action(detail=False, methods=['POST'])
    def new_client(self, request):

        full_name = request.data['full_name']
        user = User.objects.get(id=request.data['user_id'])

        client = Client.objects.create(user=user, full_name=full_name)
        client.save()
        serializer = ClientSerializer(client, many=False)

        message = {'message': "Client Created", 'client': serializer.data}
        return Response(message, status=status.HTTP_200_OK)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    # @action(detail=False, methods=['POST'])
    # def book_app(self, request):

    #     day = request.data['day']
    #     start_time = request.data['start_time']
    #     end_time = request.data['end_time']
    #     trainer = request.data['trainer_id']
    #     client = request.data['client_id']
    #     time = None

    #     trainer_instance = Trainer.objects.get(id=trainer)
    #     client_instance = Client.objects.get(id=client)

    #     if not start_time or not end_time:
    #         pass
    #     else:
    #         time1 = datetime.strptime(str(end_time), '%H:%M:%S')
    #         time2 = datetime.strptime(str(start_time), '%H:%M:%S')
    #         difference = time1-time2
    #         total = 0
    #         acc = str(difference).split(":")
    #         total = total + int(acc[0]) * 60
    #         total = total + int(acc[1])
    #         time = total

    #     appointment = Appointment.objects.create(
    #         trainer=trainer_instance, client=client_instance, day=day, start_time=start_time, end_time=end_time, time=time)
    #     serializer = AppointmentSerializer(appointment, many=False)

    #     message = {'msg': "Appt Booked!", 'appointment': serializer.data}
    #     return Response(message, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def book_app(self, request):

        start_time = request.data['start_time']
        end_time = request.data['end_time']
        trainer = request.data['trainer_id']
        client = request.data['client_id']
        time = None

        day = request.data['day']

        try:
            appointment_day = AppointmentDay.objects.get(day=day)

        except AppointmentDay.DoesNotExist:
            appointment_day = AppointmentDay.objects.create(day=day)

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
            trainer=trainer_instance, client=client_instance, day=appointment_day, start_time=start_time, end_time=end_time, time=time)
        serializer = AppointmentSerializer(appointment, many=False)

        # message = {'msg': "Appt Booked!", 'appointment': serializer.data}
        message = {'msg': serializer.data}
        return Response(message, status=status.HTTP_200_OK)


class AppointmentDayViewSet(viewsets.ModelViewSet):
    queryset = AppointmentDay.objects.all()
    serializer_class = AppointmentDaySerializer

    @action(detail=False, methods=['GET'])
    def day_list(self, request):

        days = AppointmentDay.objects.all()
        print(days)

        return_days = {}

        for day in days:
            try:
                print(day)
                app = Appointment.objects.filter(day=day)
                return_days[day] = {
                    'id': app.id,
                    'day': str(app.day.day),
                    'start_time': str(app.start_time),
                    'end_time': str(app.end_time),
                    'client': app.client.full_name,
                    'trainer': app.trainer.full_name,
                    'time': app.time
                }
            except:
                return_days[day] = {
                    'id': day.id,
                    'day': '',
                    'start_time': '',
                    'end_time': '',
                    'client': '',
                    'trainer': '',
                    'time': ''
                }

        print("return days", return_days)

        # serializer = AppointmentDaySerializer(return_days, many=True)
        # serializer = DayListSerializer(return_days, many=True)

        # message = {'msg': serializer.data}
        message = {'msg': 'day_list'}
        return Response(message, status=status.HTTP_200_OK)
