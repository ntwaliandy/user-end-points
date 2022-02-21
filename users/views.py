from .models import UserDeatils
from rest_framework import viewsets
from .serializers import UserSerializer
# Create your views here.

"""
    Api View to allow us create user or get a list of all registered users
"""

class UserRecordView(viewsets.ModelViewSet):
    queryset = UserDeatils.objects.all().order_by('name')
    serializer_class = UserSerializer
