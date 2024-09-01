from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UserRUDSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profile_photo',
            'description',
            'phone_number',
            'created_at',
        ]

        extra_fields = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }
