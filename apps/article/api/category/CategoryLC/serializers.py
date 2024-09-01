from rest_framework.serializers import ModelSerializer

from apps.article.models import Category


class CategoryLCSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at']

        extra_kwargs = {
            'created_at': {'read_only': True},
            'id': {'read_only': True},
        }
