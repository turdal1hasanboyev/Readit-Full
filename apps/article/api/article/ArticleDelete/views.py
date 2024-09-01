from rest_framework.generics import DestroyAPIView

from apps.article.models import Article
from .serializer import ArticleDeleteSerializer


class ArticleDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDeleteSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Article.objects.filter(is_active=True).select_related('category', 'author').prefetch_related('tags')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save() 
