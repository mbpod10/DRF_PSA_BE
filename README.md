# PSA Backend

### Endpoints

| Endpoint                                               | Description               | Body                                                  |
| ------------------------------------------------------ | ------------------------- | ----------------------------------------------------- |
| http://127.0.0.1:8000/api/users/                       | -                         | CRUD                                                  |
| http://127.0.0.1:8000/api/users/login/                 | Login w/ token            | username, password                                    |
| http://127.0.0.1:8000/api/users/register/              | Create New User w/ Token  | username, password                                    |
| http://127.0.0.1:8000/api/users/change_password/       | Change existing password  | username, password                                    |
| http://127.0.0.1:8000/appointments/                    | -                         | CRUD                                                  |
| http://127.0.0.1:8000/appointments/book_app/           | Schedule New Appt         | day, start_time, end_time, trainer, client, time=null |
| http://127.0.0.1:8000/trainers/                        | -                         | CRUD                                                  |
| http://127.0.0.1:8000/clients/                         | -                         | CRUD                                                  |
| http://127.0.0.1:8000/days/                            | -                         | CRUD                                                  |
| http://127.0.0.1:8000/days/${YYYY-MM-DD}/appointments/ | detail view of YYYY-MM-DD | GET                                                   |

### Book Appointment

http://127.0.0.1:8000/appointments/book_app/ 

Body where `trainer_id` = id of `Trainer` model and `client_id` = id of `Client` model
```json
// raw in Postman
{
    "trainer_id": 1,
    "client_id": 1,
    "day": "2020-11-11",
    "start_time": "00:24:31",
    "end_time": null,
    "time": null
}
```

## Day-Based View As Function In Appointment Day

Create `appointments` function

```py
class AppointmentDay(models.Model):
    day = models.DateField(
        u'Day Of The Event', help_text=u'Day Of The Event')

    def no_of_appointments(self):
        appointments = Appointment.objects.filter(day=self)
        return len(appointments)

    def appointments(self):
        appointments = Appointment.objects.filter(day=self)       

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
```

add `appointments` field to `AppointmentDaySerializer` 

```py
class AppointmentDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = AppointmentDay       
        fields = ('id', 'day', 'no_of_appointments', 'appointments')
```

Go to http://127.0.0.1:8000/days/ which is our designated view for this model and get the output
```json
[
    {
        "id": 12,
        "day": "2020-11-10",
        "no_of_appointments": 2,
        "appointments": [
            {
                "id": 22,
                "start_time": "22:32:57",
                "end_time": "22:32:57",
                "client": "Stephanie Bask",
                "trainer": "Brock Podgurski",
                "time": 0
            },
            {
                "id": 23,
                "start_time": "02:33:10",
                "end_time": "22:33:11",
                "client": "Stephanie Bask",
                "trainer": "Brock Podgurski",
                "time": 1200
            }
        ]
    }
]
```

## Custom URL That Utilizes Day/Date That Returns Appointments For That Day

- In `appointments/views.py` add the following code for the `AppointmentDayViewSet`

```py
class AppointmentDayViewSet(viewsets.ModelViewSet):
    queryset = AppointmentDay.objects.all()
    serializer_class = AppointmentDaySerializer

    @action(detail=True, methods=['GET'])
    def appointments(self, request, pk='day'):

        day = AppointmentDay.objects.get(day=pk)
        serializer = AppointmentDaySerializer(day, many=False)

        message = {'day': serializer.data}
        return Response(message, status=status.HTTP_200_OK)
```

Uses {prefix}/{lookup}/[function name]

Example: http://127.0.0.1:8000/days/2020-11-18/appointments/

Response:
```json
{
    "day": {
        "id": 26,
        "day": "2020-11-18",
        "no_of_appointments": 2,
        "appointments": [
            {
                "id": 57,
                "start_time": "06:00:00",
                "end_time": "09:00:00",
                "client": " Stephanie Bask",
                "trainer": "Brock Podgurski",
                "time": 180
            },
            {
                "id": 58,
                "start_time": "11:51:10",
                "end_time": "21:51:11",
                "client": " Stephanie Bask",
                "trainer": "Brock Podgurski",
                "time": 600
            }
        ]
    }
}
```