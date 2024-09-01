from rest_framework.generics import ListCreateAPIView

from .serializers import ContactLCSerializer
from apps.contact.models import Contact


class ContactLCView(ListCreateAPIView):
    """View for creating and listing contacts."""
    
    queryset = Contact.objects.all()
    serializer_class = ContactLCSerializer

    def get_queryset(self):
        return Contact.objects.filter(is_active=True)
    