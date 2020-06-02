from core.user import User


class QueryUser:
    """all about query user"""

    @classmethod
    def all_users(cls):
        """get all users"""
        return User.objects.all()

    def current_user(self, request):
        """get current user"""
        current_user = User.objects.get(id=request.user)
        return current_user
