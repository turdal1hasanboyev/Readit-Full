from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from apps.article.models import Tag
from .serializers import TagRUDSerializer


class TagRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagRUDSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Tag.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save() 
    