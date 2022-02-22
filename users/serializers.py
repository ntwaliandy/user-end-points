
from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import UserDeatils
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')

#Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create(validated_data['first_name'], validated_data['last_name'], validated_data['username'], validated_data['password'])
        return user

#login
class LoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('incorrect credentials!!!')