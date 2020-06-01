from rest_framework import serializers
from core.user import User


class UserSerializer(serializers.ModelSerializer):
    """user serializer"""

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}
        read_only_fields = "id"
