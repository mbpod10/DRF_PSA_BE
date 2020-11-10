# PSA Backend

### Endpoints

| Endpoint                                         | Description              | Body                                                  |
| ------------------------------------------------ | ------------------------ | ----------------------------------------------------- |
| http://127.0.0.1:8000/api/users/                 | -                        | CRUD                                                  |
| http://127.0.0.1:8000/api/users/login/           | Login w/ token           | username, password                                    |
| http://127.0.0.1:8000/api/users/register/        | Create New User w/ Token | username, password                                    |
| http://127.0.0.1:8000/api/users/change_password/ | Change existing password | username, password                                    |
| http://127.0.0.1:8000/appointments/              | -                        | CRUD                                                  |
| http://127.0.0.1:8000/appointments/book_app/     | Schedule New Appt        | day, start_time, end_time, trainer, client, time=null |
| http://127.0.0.1:8000/trainers/                  | -                        | CRUD                                                  |
| http://127.0.0.1:8000/clients/                   | -                        | CRUD                                                  |

### Book Appointment

http://127.0.0.1:8000/appointments/book_app/ 

Body: 
```json
{
    "trainer_id": 1,
    "client_id": 1,
    "day": "2020-11-11",
    "start_time": "00:24:31",
    "end_time": null,
    "time": null
}
```
