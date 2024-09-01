from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.user.models import Client
from .serializers import ClientRUDSerializer


class ClientRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientRUDSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser, IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    