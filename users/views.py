from rest_framework import viewsets, generics
from users.models import User
from users.serializer import UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]

class UserCreateAPIView(generics.CreateAPIView):
    """creating user"""
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """ list of users """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ list of user """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """ updating for user """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(generics.DestroyAPIView):
    """ deleting a user """
    serializer_class = UserSerializer
    queryset = User.objects.all()
