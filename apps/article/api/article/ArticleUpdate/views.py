from rest_framework.generics import UpdateAPIView

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.article.models import Article
from .serializer import ArticleUpdateSerializer


class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('category', 'author').prefetch_related('tags')
