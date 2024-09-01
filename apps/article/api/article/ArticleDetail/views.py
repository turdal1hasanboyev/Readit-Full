from rest_framework.generics import RetrieveAPIView

from apps.article.models import Article
from .serializer import ArticleDetailSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Article.objects.filter(is_active=True).select_related('category', 'author').prefetch_related('tags')
