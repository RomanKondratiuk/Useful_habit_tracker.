from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]