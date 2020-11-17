from rest_framework import serializers
from django.contrib.auth.models import User
# from appointments.serializers import ClientSerializer
# from appointments.models import Client


class UserSerializer(serializers.ModelSerializer):

    # client = ClientSerializer(read_only=True, many=False)

    class Meta:
        model = User

        # fields = ('id', 'username', 'password', 'client')
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
