from rest_framework.generics import CreateAPIView

from apps.article.models import Comment
from .serializers import CommentCreateSerializer


class CommentCreateView(CreateAPIView):
    """
    Create a new comment
    """

    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Comment.objects.filter(is_active=True).select_related('user', 'article')
    