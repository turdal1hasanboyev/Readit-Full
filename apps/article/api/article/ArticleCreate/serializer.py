from rest_framework.serializers import ModelSerializer

from apps.article.models import Article


class ArticleCreateSerializer(ModelSerializer):
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

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }
