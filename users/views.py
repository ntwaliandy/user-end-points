
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
# Create your views here.

"""
    Api View to allow us create user or get a list of all registered users
"""
class UserRecordView(APIView):

    permission_classes = [IsAdminUser]
    
    # Getting the list of all users

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)


    # creating a new user with the required information.

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages
            },
            status=status.HTTP_400_BAD_REQUEST
        )