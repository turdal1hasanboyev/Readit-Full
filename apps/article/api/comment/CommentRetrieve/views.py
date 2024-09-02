from rest_framework.generics import RetrieveAPIView

from apps.article.models import Comment
from .serializers import CommentRetrieveSerializer


class CommentRetrieveView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentRetrieveSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        return Comment.objects.filter(is_active=True).select_related('user', 'article')
