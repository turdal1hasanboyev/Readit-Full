from rest_framework.generics import UpdateAPIView

from apps.article.models import Comment
from .serializer import CommentUpdateSerializer


class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'article')
