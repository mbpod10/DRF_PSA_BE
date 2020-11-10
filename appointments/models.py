# from .serializers import AppointmentSerializer
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime


from django.utils.timezone import now
# Create your models here.


class Trainer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='trainer')
    full_name = models.CharField(max_length=32)

    def __str__(self):
        return self.full_name


class Client(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='client')
    full_name = models.CharField(max_length=32)

    def __str__(self):
        return self.full_name


class AppointmentDay(models.Model):
    day = models.DateField(
        u'Day Of The Event', help_text=u'Day Of The Event')

    def no_of_appointments(self):
        appointments = Appointment.objects.filter(day=self)
        return len(appointments)

    def appointments(self):
        appointments = Appointment.objects.filter(day=self)

        print(len(appointments))

        return_days = []

        for acc in appointments:

            return_days.append({
                'id': acc.id,
                'start_time': str(acc.start_time),
                'end_time': str(acc.end_time),
                'client': acc.client.full_name,
                'trainer': acc.trainer.full_name,
                'time': acc.time
            })

        return return_days

    def __str__(self):
        return str(self.day) + " ( id-" + str(self.id) + " ) "


class Appointment(models.Model):
    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, related_name='trainer')
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='client')
    day = models.ForeignKey(
        AppointmentDay, related_name='app_day', on_delete=models.CASCADE)
    # day = models.DateField(
    #     u'Day Of The Event', help_text=u'Day Of The Event')
    start_time = models.TimeField(
        u'Starting Time', help_text=u'Starting Time')
    end_time = models.TimeField(
        u'Final Time', help_text='Final Time', blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    def clean(self):
        self.get_time()

    def get_time(self):
        if not self.start_time or not self.end_time:
            pass
        else:
            time1 = datetime.strptime(str(self.end_time), '%H:%M:%S')
            time2 = datetime.strptime(str(self.start_time), '%H:%M:%S')
            difference = time1-time2
            total = 0
            acc = str(difference).split(":")
            total = total + int(acc[0]) * 60
            total = total + int(acc[1])
            self.time = total
            self.save()

    def __str__(self):
        if self.end_time:
            return str(self.client.full_name).split(" ")[1] + " " + str(self.day) + " (" + str(self.start_time) + ") " + str(self.trainer.full_name).split(" ")[1] + " CLOSED "
        else:
            return str(self.client.full_name).split(" ")[1] + " " + str(self.day) + " (" + str(self.start_time) + ") " + str(self.trainer.full_name).split(" ")[1] + " OPEN"


# class DayListModel(models.Model):
#     trainer = models.CharField(max_length=256)
#     client = models.CharField(max_length=256)
#     start_time = models.CharField(max_length=256)
#     end_time = models.CharField(max_length=256)
#     day = models.CharField(max_length=256)
#     time = models.PositiveIntegerField()
