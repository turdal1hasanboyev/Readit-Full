from rest_framework.generics import CreateAPIView

from apps.article.models import Article
from .serializer import ArticleCreateSerializer

from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Article.objects.filter(is_active=True).select_related('category', 'author').prefetch_related('tags')
