from rest_framework.serializers import ModelSerializer

from apps.article.models import Comment


class CommentDestroySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'article',
            'name',
            'message',
            'web_site',
            'email',
            'created_at',
        ]
