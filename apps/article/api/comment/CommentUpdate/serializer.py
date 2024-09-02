from rest_framework.serializers import ModelSerializer

from apps.article.models import Comment


class CommentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'article',
            'user',
            'name',
            'message',
            'web_site',
            'email',
            "created_at",
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'user': {'read_only': True},
            'article': {'read_only': True},
        }
