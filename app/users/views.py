from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.user import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """create new user """

    serializer_class = UserSerializer
    permission_class = AllowAny
    queryset = User.objects.all()

    def get(self, request):
        """list all users"""
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset)
        return Response({"data": serializer.data})
