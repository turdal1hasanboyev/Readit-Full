from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from apps.article.models import Tag
from .serializers import TagLCSerializer


class TagLCView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagLCSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    