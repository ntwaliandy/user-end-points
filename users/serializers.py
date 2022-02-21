
from rest_framework import serializers

from users.models import UserDeatils



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDeatils
        fields = (
            'name',
            'age',
            'phone_number',
            'email',
            'password',
        )