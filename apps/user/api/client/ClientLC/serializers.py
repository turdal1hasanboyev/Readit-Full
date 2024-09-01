from rest_framework.serializers import ModelSerializer

from apps.user.models import Client


class ClientLCSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'name',
            'image',
            'description',
            'job',
            'created_at',
        ]

        extra_fields = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }
