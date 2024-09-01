from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializers import ContactRUDSerializer
from apps.contact.models import Contact


class ContactRUDView(RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting a contact.
    """

    queryset = Contact.objects.all()
    serializer_class = ContactRUDSerializer
    lookup_field = 'name'

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
