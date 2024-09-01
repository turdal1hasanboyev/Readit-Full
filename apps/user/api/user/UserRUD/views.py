from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.user.models import User
from .serializers import UserRUDSerializer


class UserRUDView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRUDSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
    
    def get_queryset(self):
        return User.objects.filter(is_active=True)
    