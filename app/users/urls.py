from django.urls import path
from .views import CreateUserView, UserViewSet

app_name = "user"

urlpatterns = [
    path("user", CreateUserView.as_view(), name="create"),
    path(
        "user/<int:pk>", UserViewSet.as_view({"get": "retrieve"}), name="user-details",
    ),
]
