from rest_framework.serializers import ModelSerializer

from apps.article.models import Comment
from apps.article.api.article.ArticleDetail.serializer import ArticleDetailSerializer
from apps.user.api.user.UserLC.serializers import UserLCSerializer


class CommentListSerializer(ModelSerializer):
    article = ArticleDetailSerializer(read_only=True)
    user = UserLCSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'article', 'user', 'name', 'message', 'web_site', 'email', 'created_at']
