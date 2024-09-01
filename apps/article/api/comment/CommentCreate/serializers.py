from rest_framework.serializers import ModelSerializer

from apps.article.models import Comment
from apps.user.api.user.UserLC.serializers import UserLCSerializer


class CommentCreateSerializer(ModelSerializer):
    user = UserLCSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'article', 'user', 'name', 'message', 'web_site', 'email', 'created_at']

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }