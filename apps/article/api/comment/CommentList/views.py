from rest_framework.generics import ListAPIView

from apps.article.models import Comment
from .serializers import CommentListSerializer


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    # pagination_class = None
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'article')
