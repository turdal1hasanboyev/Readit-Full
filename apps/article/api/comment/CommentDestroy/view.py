from rest_framework.generics import DestroyAPIView

from apps.article.models import Comment
from .serializer import CommentDestroySerializer


class CommentDestroyView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDestroySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Comment.objects.filter(is_active=True).select_related('user', 'article')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
