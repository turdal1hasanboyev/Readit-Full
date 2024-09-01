from rest_framework.generics import ListCreateAPIView

from apps.user.models import User
from .serializers import UserLCSerializer


class UserLCView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLCSerializer
    
    def get_queryset(self):
        return User.objects.filter(is_active=True)
    