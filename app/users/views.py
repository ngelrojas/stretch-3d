from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.query_core.queryUser import QueryUser
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """create new user """

    serializer_class = UserSerializer
    permission_class = AllowAny


class UserViewSet(viewsets.ModelViewSet):
    """all about user update, list and retrieve"""

    serializer_class = UserSerializer
    queryset = QueryUser.all_users()

    def retrieve(self, request, pk):
        """
            retrieve current user
        """
        current_user = QueryUser.current_user(self, request)
        serializer = self.serializer_class(current_user)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
