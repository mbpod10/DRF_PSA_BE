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

    def __str__(self):
        return str(self.day)


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
