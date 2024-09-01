from rest_framework.serializers import ModelSerializer

from apps.article.models import Article


class ArticleDeleteSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'category',
            'tags',
            'image',
            'author',
            'views',
            "created_at",
        ]
