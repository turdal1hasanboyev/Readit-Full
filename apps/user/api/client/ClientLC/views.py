from rest_framework.generics import ListCreateAPIView

from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from apps.user.models import Client
from .serializers import ClientLCSerializer


class ClientLCView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientLCSerializer
    pagination_class = None
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return Client.objects.filter(is_active=True)
    