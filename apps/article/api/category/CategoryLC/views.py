from rest_framework.generics import ListCreateAPIView

from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.article.models import Category
from .serializers import CategoryLCSerializer


class CategoryLCView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryLCSerializer
    pagination_class = None
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(is_active=True)
    