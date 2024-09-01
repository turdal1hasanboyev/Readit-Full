from rest_framework.serializers import ModelSerializer

from apps.article.models import Article

from apps.article.api.category.CategoryLC.serializers import CategoryLCSerializer
from apps.article.api.tag.TagLC.serializers import TagLCSerializer
from apps.user.api.user.UserLC.serializers import UserLCSerializer


class ArticleListSerializer(ModelSerializer):
    category = CategoryLCSerializer(read_only=True)
    tags = TagLCSerializer(read_only=True, many=True)
    author = UserLCSerializer(read_only=True)

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
